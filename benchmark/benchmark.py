"""
benchmark.py

Coding correctness benchmark for llama.cpp / Qwen2.5-Coder.

Requirements:
    pip install requests

Expected project structure:

    benchmark/
        benchmark.py
        problems.py
        results/

problems.py must define:

    PROBLEMS = [
        {
            "name": "is_prime",
            "category": "easy",
            "prompt": "...",
            "tests": [
                ("is_prime(2)", True),
                ...
            ]
        }
    ]

Start llama-server before running this program.

Example:

    llama-server.exe -m MODEL.gguf -ngl 0 -c 4096 --port 8080

Then:

    python benchmark.py
"""

from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests

from problems import PROBLEMS


# ============================================================
# CONFIGURATION
# ============================================================

LLAMA_BASE_URL = "http://127.0.0.1:8080"
CHAT_URL = f"{LLAMA_BASE_URL}/v1/chat/completions"

# This is only used as a report label.
# Change it before each benchmark run.
MODEL_LABEL = "qwen2.5-coder-3b-Q4_K_M"

RESULTS_DIR = Path("results")

REQUEST_TIMEOUT_SECONDS = 1800
TEST_TIMEOUT_SECONDS = 10

MAX_TOKENS = 700
TEMPERATURE = 0.0
SEED = 42


SYSTEM_PROMPT = """
You are being evaluated on Python programming ability.

Implement exactly what the user requests.

Return only executable Python source code.

Do not:
- repeat the question
- repeat the requirements
- provide explanations
- provide headings
- provide bullet points
- provide introductory text
- provide concluding text

Markdown code fences are unnecessary.
""".strip()


# ============================================================
# SERVER
# ============================================================

def check_server() -> bool:
    """
    Return True if llama-server is reachable.
    """

    try:
        response = requests.get(
            f"{LLAMA_BASE_URL}/health",
            timeout=5,
        )

        return response.status_code == 200

    except requests.RequestException:
        return False


# ============================================================
# GENERATION
# ============================================================

def generate_code(prompt: str) -> dict[str, Any]:
    """
    Send a problem to llama.cpp's OpenAI-compatible chat API.

    Returns generation metadata and the raw model response.
    """

    payload = {
        "messages": [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        "temperature": TEMPERATURE,
        "seed": SEED,
        "max_tokens": MAX_TOKENS,
    }

    start_time = time.perf_counter()

    response = requests.post(
        CHAT_URL,
        json=payload,
        timeout=REQUEST_TIMEOUT_SECONDS,
    )

    elapsed = time.perf_counter() - start_time

    response.raise_for_status()

    data = response.json()

    try:
        raw_text = data["choices"][0]["message"]["content"]

    except (KeyError, IndexError, TypeError) as exc:
        raise RuntimeError(
            "Unexpected response from llama-server:\n"
            + json.dumps(data, indent=2)
        ) from exc

    if not isinstance(raw_text, str):
        raise RuntimeError(
            "llama-server returned non-string content."
        )

    usage = data.get("usage", {})

    if not isinstance(usage, dict):
        usage = {}

    prompt_tokens = usage.get("prompt_tokens")
    completion_tokens = usage.get("completion_tokens")

    approximate_tps = None

    if (
        isinstance(completion_tokens, int)
        and completion_tokens > 0
        and elapsed > 0
    ):
        approximate_tps = completion_tokens / elapsed

    return {
        "raw_response": raw_text,
        "generation_seconds": elapsed,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "approx_tokens_per_second": approximate_tps,
    }


# ============================================================
# PYTHON VALIDATION
# ============================================================

def validate_python(code: str) -> tuple[bool, str | None]:
    """
    Validate Python syntax without executing the code.
    """

    try:
        ast.parse(code)

        return True, None

    except SyntaxError as exc:
        return False, str(exc)


# ============================================================
# CODE EXTRACTION
# ============================================================

def extract_markdown_blocks(text: str) -> list[str]:
    """
    Extract fenced code blocks.

    Supports:

        ```python
        ...
        ```

        ```py
        ...
        ```

        ```
        ...
        ```
    """

    pattern = re.compile(
        r"```(?:python|py)?\s*\n?(.*?)```",
        re.IGNORECASE | re.DOTALL,
    )

    return [
        block.strip()
        for block in pattern.findall(text)
        if block.strip()
    ]


def remove_markdown_fences(text: str) -> str:
    """
    Remove simple opening/closing Markdown fences.
    """

    text = re.sub(
        r"^\s*```(?:python|py)?\s*",
        "",
        text,
        flags=re.IGNORECASE,
    )

    text = re.sub(
        r"\s*```\s*$",
        "",
        text,
    )

    return text.strip()


def find_valid_suffix(text: str) -> str | None:
    """
    Handle responses containing prose before valid Python.

    Example:

        Here is the implementation:
        def is_prime(n):
            ...

    The function tries likely Python starting lines and returns
    the first syntactically valid suffix.
    """

    lines = text.splitlines()

    starters = (
        "def ",
        "async def ",
        "class ",
        "import ",
        "from ",
        "@",
    )

    candidate_indexes = []

    for index, line in enumerate(lines):

        stripped = line.lstrip()

        if stripped.startswith(starters):
            candidate_indexes.append(index)

    for index in candidate_indexes:

        candidate = "\n".join(
            lines[index:]
        ).strip()

        candidate = remove_markdown_fences(candidate)

        valid, _ = validate_python(candidate)

        if valid:
            return candidate

    return None


def extract_python_code(
    raw_response: str,
) -> tuple[str, str]:
    """
    Convert the model response into executable Python.

    Returns:

        (code, extraction_method)

    extraction_method can be:

        raw
        markdown
        prose_removed

    Raises ValueError when valid Python cannot be recovered.
    """

    if not raw_response:
        raise ValueError(
            "The model returned an empty response."
        )

    text = raw_response.strip()

    if not text:
        raise ValueError(
            "The model returned an empty response."
        )

    # --------------------------------------------------------
    # 1. Entire response already valid Python
    # --------------------------------------------------------

    valid, _ = validate_python(text)

    if valid:
        return text, "raw"

    # --------------------------------------------------------
    # 2. Look for valid Markdown code block
    # --------------------------------------------------------

    blocks = extract_markdown_blocks(text)

    for block in blocks:

        valid, _ = validate_python(block)

        if valid:
            return block, "markdown"

    # --------------------------------------------------------
    # 3. Remove simple surrounding fences
    # --------------------------------------------------------

    without_fences = remove_markdown_fences(text)

    valid, _ = validate_python(without_fences)

    if valid:
        return without_fences, "markdown"

    # --------------------------------------------------------
    # 4. Remove prose appearing before the Python
    # --------------------------------------------------------

    candidate = find_valid_suffix(text)

    if candidate is not None:
        return candidate, "prose_removed"

    # --------------------------------------------------------
    # Unable to recover valid Python
    # --------------------------------------------------------

    _, syntax_error = validate_python(text)

    raise ValueError(
        "Could not extract valid Python source code. "
        f"Initial syntax error: {syntax_error}"
    )


# ============================================================
# FORMAT COMPLIANCE
# ============================================================

def is_format_compliant(raw_response: str) -> bool:
    """
    A response is considered format compliant when the complete
    response itself is valid Python.

    Markdown/prose can still be recovered by the extractor,
    but will count as a formatting failure.
    """

    valid, _ = validate_python(
        raw_response.strip()
    )

    return valid


# ============================================================
# UNIT TEST EXECUTION
# ============================================================

def run_single_test(
    code: str,
    expression: str,
    expected: Any,
) -> dict[str, Any]:
    """
    Execute one hidden unit test in a separate Python process.

    WARNING:
    Generated model code is untrusted code.

    This subprocess + timeout design is suitable for controlled
    toy benchmark problems, but it is NOT a security sandbox.
    """

    expected_literal = repr(expected)

    test_script = (
        code
        + "\n\n"
        + "import sys\n"
        + "\n"
        + "try:\n"
        + f"    __benchmark_actual = ({expression})\n"
        + f"    __benchmark_expected = {expected_literal}\n"
        + "\n"
        + "    if __benchmark_actual == __benchmark_expected:\n"
        + "        print('TEST_PASS')\n"
        + "        sys.exit(0)\n"
        + "\n"
        + "    print('TEST_FAIL')\n"
        + "    print('EXPECTED:', repr(__benchmark_expected))\n"
        + "    print('ACTUAL:', repr(__benchmark_actual))\n"
        + "    sys.exit(1)\n"
        + "\n"
        + "except Exception as exc:\n"
        + "    print('TEST_EXCEPTION')\n"
        + "    print(type(exc).__name__ + ':', str(exc))\n"
        + "    sys.exit(2)\n"
    )

    temp_path = None

    try:

        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8",
        ) as temp_file:

            temp_file.write(test_script)

            temp_path = temp_file.name

        start_time = time.perf_counter()

        completed = subprocess.run(
            [
                sys.executable,
                temp_path,
            ],
            capture_output=True,
            text=True,
            timeout=TEST_TIMEOUT_SECONDS,
        )

        elapsed = time.perf_counter() - start_time

        return {
            "passed": completed.returncode == 0,
            "return_code": completed.returncode,
            "stdout": completed.stdout.strip(),
            "stderr": completed.stderr.strip(),
            "timeout": False,
            "execution_seconds": elapsed,
        }

    except subprocess.TimeoutExpired:

        return {
            "passed": False,
            "return_code": None,
            "stdout": "",
            "stderr": "TEST_TIMEOUT",
            "timeout": True,
            "execution_seconds": TEST_TIMEOUT_SECONDS,
        }

    finally:

        if temp_path is not None:

            try:
                os.remove(temp_path)

            except OSError:
                pass


def run_tests(
    code: str,
    tests: list,
) -> dict[str, Any]:
    """
    Run every hidden unit test for one generated solution.
    """

    details = []

    for test_number, test in enumerate(
        tests,
        start=1,
    ):

        if (
            not isinstance(test, (tuple, list))
            or len(test) != 2
        ):
            raise ValueError(
                f"Invalid test #{test_number}: "
                "each test must be "
                "(expression, expected)."
            )

        expression, expected = test

        if not isinstance(expression, str):
            raise ValueError(
                f"Invalid expression in test "
                f"#{test_number}."
            )

        result = run_single_test(
            code=code,
            expression=expression,
            expected=expected,
        )

        result.update(
            {
                "test_number": test_number,
                "expression": expression,
                "expected": expected,
            }
        )

        details.append(result)

    passed = sum(
        1
        for result in details
        if result["passed"]
    )

    total = len(details)

    pass_rate = (
        (passed / total) * 100.0
        if total > 0
        else 0.0
    )

    return {
        "all_passed": (
            total > 0
            and passed == total
        ),
        "passed": passed,
        "total": total,
        "pass_rate": pass_rate,
        "details": details,
    }


# ============================================================
# BENCHMARK ONE PROBLEM
# ============================================================

def benchmark_problem(
    problem: dict[str, Any],
) -> dict[str, Any]:

    name = problem.get(
        "name",
        "unnamed_problem",
    )

    category = problem.get(
        "category",
        "unknown",
    )

    prompt = problem.get("prompt")
    tests = problem.get("tests")

    print()
    print("=" * 72)
    print(f"PROBLEM: {name}")
    print(f"CATEGORY: {category}")
    print("=" * 72)

    record = {
        "name": name,
        "category": category,
        "status": "not_started",
        "format_compliant": False,
        "syntax_valid": False,
        "extraction_method": None,
        "raw_response": None,
        "extracted_code": None,
        "generation_seconds": None,
        "prompt_tokens": None,
        "completion_tokens": None,
        "approx_tokens_per_second": None,
        "tests_passed": 0,
        "tests_total": (
            len(tests)
            if isinstance(tests, list)
            else 0
        ),
        "test_pass_rate": 0.0,
        "all_tests_passed": False,
        "error": None,
        "test_details": [],
    }

    # --------------------------------------------------------
    # Validate problem definition
    # --------------------------------------------------------

    if not isinstance(prompt, str) or not prompt.strip():

        record["status"] = "invalid_problem"

        record["error"] = (
            "Problem has no valid prompt."
        )

        print(
            "ERROR:",
            record["error"],
        )

        return record

    if not isinstance(tests, list) or not tests:

        record["status"] = "invalid_problem"

        record["error"] = (
            "Problem has no unit tests."
        )

        print(
            "ERROR:",
            record["error"],
        )

        return record

    # --------------------------------------------------------
    # Generate
    # --------------------------------------------------------

    try:

        generation = generate_code(prompt)

    except Exception as exc:

        record["status"] = "generation_failure"
        record["error"] = str(exc)

        print()
        print("GENERATION FAILED")
        print(str(exc))

        return record

    raw_response = generation["raw_response"]

    record["raw_response"] = raw_response

    record["generation_seconds"] = (
        generation["generation_seconds"]
    )

    record["prompt_tokens"] = (
        generation["prompt_tokens"]
    )

    record["completion_tokens"] = (
        generation["completion_tokens"]
    )

    record["approx_tokens_per_second"] = (
        generation[
            "approx_tokens_per_second"
        ]
    )

    # --------------------------------------------------------
    # Display raw response
    # --------------------------------------------------------

    print()
    print("RAW MODEL RESPONSE")
    print("-" * 72)
    print(raw_response)
    print("-" * 72)

    # --------------------------------------------------------
    # Formatting
    # --------------------------------------------------------

    record["format_compliant"] = (
        is_format_compliant(raw_response)
    )

    # --------------------------------------------------------
    # Extract code
    # --------------------------------------------------------

    try:

        code, method = extract_python_code(
            raw_response
        )

    except ValueError as exc:

        record["status"] = "extraction_failure"
        record["error"] = str(exc)

        print()
        print("CODE EXTRACTION FAILED")
        print(str(exc))

        return record

    record["extracted_code"] = code

    record["extraction_method"] = method

    print()
    print("EXTRACTED PYTHON")
    print("-" * 72)
    print(code)
    print("-" * 72)

    print(
        f"Extraction method: {method}"
    )

    # --------------------------------------------------------
    # Validate syntax
    # --------------------------------------------------------

    syntax_valid, syntax_error = (
        validate_python(code)
    )

    record["syntax_valid"] = syntax_valid

    if not syntax_valid:

        record["status"] = "syntax_failure"
        record["error"] = syntax_error

        print()
        print("SYNTAX FAILURE")
        print(syntax_error)

        return record

    print("Syntax: VALID")

    # --------------------------------------------------------
    # Execute tests
    # --------------------------------------------------------

    try:

        test_result = run_tests(
            code,
            tests,
        )

    except Exception as exc:

        record["status"] = "test_harness_failure"
        record["error"] = str(exc)

        print()
        print("TEST HARNESS FAILURE")
        print(str(exc))

        return record

    record["tests_passed"] = (
        test_result["passed"]
    )

    record["tests_total"] = (
        test_result["total"]
    )

    record["test_pass_rate"] = (
        test_result["pass_rate"]
    )

    record["all_tests_passed"] = (
        test_result["all_passed"]
    )

    record["test_details"] = (
        test_result["details"]
    )

    # --------------------------------------------------------
    # Display tests
    # --------------------------------------------------------

    print()
    print("UNIT TESTS")
    print("-" * 72)

    for result in test_result["details"]:

        test_number = result["test_number"]

        if result["passed"]:

            print(
                f"Test {test_number}: PASS"
            )

        else:

            print(
                f"Test {test_number}: FAIL"
            )

            print(
                "  Expression:",
                result["expression"],
            )

            print(
                "  Expected:",
                repr(result["expected"]),
            )

            if result["stdout"]:

                print(
                    "  STDOUT:",
                    result["stdout"],
                )

            if result["stderr"]:

                print(
                    "  STDERR:",
                    result["stderr"],
                )

    print("-" * 72)

    print(
        f"Tests passed: "
        f"{test_result['passed']}/"
        f"{test_result['total']}"
    )

    print(
        f"Unit-test correctness: "
        f"{test_result['pass_rate']:.1f}%"
    )

    # --------------------------------------------------------
    # Timing
    # --------------------------------------------------------

    print(
        f"Generation time: "
        f"{generation['generation_seconds']:.2f} sec"
    )

    if generation["completion_tokens"] is not None:

        print(
            "Completion tokens:",
            generation["completion_tokens"],
        )

    if (
        generation[
            "approx_tokens_per_second"
        ]
        is not None
    ):

        print(
            "Approx generation speed: "
            f"{generation['approx_tokens_per_second']:.2f} "
            "tokens/sec"
        )

    # --------------------------------------------------------
    # Final status
    # --------------------------------------------------------

    if test_result["all_passed"]:

        record["status"] = "pass"

        print("RESULT: PASS")

    else:

        record["status"] = "unit_test_failure"

        print("RESULT: FAIL")

    return record


# ============================================================
# SUMMARY
# ============================================================

def calculate_summary(
    results: list[dict[str, Any]],
) -> dict[str, Any]:

    total_problems = len(results)

    problems_passed = sum(
        1
        for result in results
        if result["all_tests_passed"]
    )

    syntax_valid = sum(
        1
        for result in results
        if result["syntax_valid"]
    )

    format_compliant = sum(
        1
        for result in results
        if result["format_compliant"]
    )

    tests_total = sum(
        result["tests_total"]
        for result in results
    )

    tests_passed = sum(
        result["tests_passed"]
        for result in results
    )

    generation_times = [
        result["generation_seconds"]
        for result in results
        if isinstance(
            result["generation_seconds"],
            (int, float),
        )
    ]

    speeds = [
        result["approx_tokens_per_second"]
        for result in results
        if isinstance(
            result["approx_tokens_per_second"],
            (int, float),
        )
    ]

    problem_correctness = (
        problems_passed
        / total_problems
        * 100.0
        if total_problems
        else 0.0
    )

    unit_test_correctness = (
        tests_passed
        / tests_total
        * 100.0
        if tests_total
        else 0.0
    )

    syntax_rate = (
        syntax_valid
        / total_problems
        * 100.0
        if total_problems
        else 0.0
    )

    format_rate = (
        format_compliant
        / total_problems
        * 100.0
        if total_problems
        else 0.0
    )

    average_generation_time = (
        sum(generation_times)
        / len(generation_times)
        if generation_times
        else None
    )

    average_speed = (
        sum(speeds)
        / len(speeds)
        if speeds
        else None
    )

    return {
        "total_problems": total_problems,
        "problems_passed": problems_passed,
        "problem_correctness_percent":
            problem_correctness,
        "total_unit_tests": tests_total,
        "unit_tests_passed": tests_passed,
        "unit_test_correctness_percent":
            unit_test_correctness,
        "syntax_valid_percent":
            syntax_rate,
        "format_compliance_percent":
            format_rate,
        "average_generation_seconds":
            average_generation_time,
        "average_approx_tokens_per_second":
            average_speed,
    }


# ============================================================
# REPORT
# ============================================================

def make_json_safe(value: Any) -> Any:
    """
    Convert values that are not directly JSON serializable.
    """

    try:
        json.dumps(value)
        return value

    except (TypeError, ValueError):
        return repr(value)


def sanitize_results_for_json(
    results: list[dict[str, Any]],
) -> list[dict[str, Any]]:

    clean_results = []

    for result in results:

        clean_result = dict(result)

        clean_tests = []

        for test in result.get(
            "test_details",
            []
        ):

            clean_test = dict(test)

            clean_test["expected"] = (
                make_json_safe(
                    clean_test.get("expected")
                )
            )

            clean_tests.append(clean_test)

        clean_result["test_details"] = (
            clean_tests
        )

        clean_results.append(
            clean_result
        )

    return clean_results


def save_report(
    results: list[dict[str, Any]],
    summary: dict[str, Any],
) -> Path:

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    safe_model_name = re.sub(
        r"[^A-Za-z0-9_.-]",
        "_",
        MODEL_LABEL,
    )

    report_path = (
        RESULTS_DIR
        / f"{safe_model_name}_{timestamp}.json"
    )

    report = {
        "benchmark": {
            "model_label": MODEL_LABEL,
            "timestamp": (
                datetime.now().isoformat()
            ),
            "llama_base_url":
                LLAMA_BASE_URL,
            "temperature":
                TEMPERATURE,
            "seed":
                SEED,
            "max_tokens":
                MAX_TOKENS,
            "test_timeout_seconds":
                TEST_TIMEOUT_SECONDS,
        },

        "summary": summary,

        "results":
            sanitize_results_for_json(
                results
            ),
    }

    with report_path.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            report,
            file,
            indent=2,
            ensure_ascii=False,
        )

    return report_path


# ============================================================
# PROBLEM DEFINITION CHECK
# ============================================================

def validate_problems() -> None:
    """
    Validate problems.py before contacting the model.
    """

    if not isinstance(PROBLEMS, list):

        raise TypeError(
            "PROBLEMS must be a list."
        )

    if not PROBLEMS:

        raise ValueError(
            "PROBLEMS is empty."
        )

    for index, problem in enumerate(
        PROBLEMS,
        start=1,
    ):

        if not isinstance(problem, dict):

            raise TypeError(
                f"Problem #{index} "
                "must be a dictionary."
            )

        if not isinstance(
            problem.get("name"),
            str,
        ):

            raise ValueError(
                f"Problem #{index} "
                "has no valid name."
            )

        if not isinstance(
            problem.get("prompt"),
            str,
        ):

            raise ValueError(
                f"Problem "
                f"{problem.get('name')} "
                "has no valid prompt."
            )

        tests = problem.get("tests")

        if not isinstance(tests, list):

            raise ValueError(
                f"Problem "
                f"{problem.get('name')} "
                "has no tests list."
            )

        if not tests:

            raise ValueError(
                f"Problem "
                f"{problem.get('name')} "
                "has no tests."
            )

        for test_number, test in enumerate(
            tests,
            start=1,
        ):

            if (
                not isinstance(
                    test,
                    (tuple, list),
                )
                or len(test) != 2
            ):

                raise ValueError(
                    f"Problem "
                    f"{problem.get('name')} "
                    f"test #{test_number} "
                    "must be "
                    "(expression, expected)."
                )


# ============================================================
# MAIN
# ============================================================

def main() -> int:

    print()
    print("=" * 72)
    print("QWEN CODING QUANTIZATION BENCHMARK")
    print("=" * 72)

    print(
        f"Model label : {MODEL_LABEL}"
    )

    print(
        f"Server      : {LLAMA_BASE_URL}"
    )

    print(
        f"Temperature : {TEMPERATURE}"
    )

    print(
        f"Seed        : {SEED}"
    )

    # --------------------------------------------------------
    # Validate problems.py
    # --------------------------------------------------------

    try:

        validate_problems()

    except Exception as exc:

        print()
        print(
            "ERROR IN problems.py:"
        )

        print(str(exc))

        return 1

    print(
        f"Problems    : {len(PROBLEMS)}"
    )

    # --------------------------------------------------------
    # Check server
    # --------------------------------------------------------

    print()
    print(
        "Checking llama-server..."
    )

    if not check_server():

        print()
        print(
            "ERROR: llama-server is not reachable at:"
        )

        print(
            LLAMA_BASE_URL
        )

        print()
        print(
            "Start llama-server first."
        )

        print()
        print(
            "Example:"
        )

        print(
            'llama-server.exe '
            '-m "MODEL.gguf" '
            '-ngl 0 '
            '-c 4096 '
            '--port 8080'
        )

        return 1

    print(
        "llama-server is ready."
    )

    # --------------------------------------------------------
    # Benchmark
    # --------------------------------------------------------

    results = []

    benchmark_start = (
        time.perf_counter()
    )

    for problem in PROBLEMS:

        result = benchmark_problem(
            problem
        )

        results.append(result)

    total_benchmark_seconds = (
        time.perf_counter()
        - benchmark_start
    )

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    summary = calculate_summary(
        results
    )

    summary[
        "total_benchmark_seconds"
    ] = total_benchmark_seconds

    print()
    print("=" * 72)
    print("FINAL BENCHMARK RESULTS")
    print("=" * 72)

    print(
        "Problems passed: "
        f"{summary['problems_passed']}/"
        f"{summary['total_problems']}"
    )

    print(
        "Problem correctness: "
        f"{summary['problem_correctness_percent']:.1f}%"
    )

    print()

    print(
        "Unit tests passed: "
        f"{summary['unit_tests_passed']}/"
        f"{summary['total_unit_tests']}"
    )

    print(
        "Unit-test correctness: "
        f"{summary['unit_test_correctness_percent']:.1f}%"
    )

    print()

    print(
        "Syntax validity: "
        f"{summary['syntax_valid_percent']:.1f}%"
    )

    print(
        "Format compliance: "
        f"{summary['format_compliance_percent']:.1f}%"
    )

    if (
        summary[
            "average_generation_seconds"
        ]
        is not None
    ):

        print(
            "Average generation time: "
            f"{summary['average_generation_seconds']:.2f} sec"
        )

    if (
        summary[
            "average_approx_tokens_per_second"
        ]
        is not None
    ):

        print(
            "Approx average generation speed: "
            f"{summary['average_approx_tokens_per_second']:.2f} "
            "tokens/sec"
        )

    print(
        "Total benchmark time: "
        f"{total_benchmark_seconds:.2f} sec"
    )

    # --------------------------------------------------------
    # Save report
    # --------------------------------------------------------

    try:

        report_path = save_report(
            results,
            summary,
        )

    except Exception as exc:

        print()
        print(
            "WARNING: benchmark completed, "
            "but JSON report could not be saved."
        )

        print(str(exc))

        return 1

    print()
    print(
        "JSON report:"
    )

    print(
        report_path.resolve()
    )

    print()
    print("=" * 72)

    return 0


if __name__ == "__main__":
    sys.exit(main())