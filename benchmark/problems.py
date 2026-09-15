PROBLEMS = [
    {
        "name": "is_prime",
        "prompt": """
Write a Python function:

def is_prime(n):

Return True if n is prime, otherwise False.

Requirements:
- n < 2 must return False.
- Do not use external libraries.
- Return ONLY Python code.
- Do not use Markdown code fences.
""",
        "tests": [
            ("is_prime(-1)", False),
            ("is_prime(0)", False),
            ("is_prime(1)", False),
            ("is_prime(2)", True),
            ("is_prime(3)", True),
            ("is_prime(4)", False),
            ("is_prime(17)", True),
            ("is_prime(25)", False),
            ("is_prime(97)", True),
            ("is_prime(100)", False),
        ]
    },

    {
        "name": "binary_search",
        "prompt": """
Write a Python function:

def binary_search(arr, target):

The input array is sorted.
Return the index of target.
Return -1 if target does not exist.

Return ONLY Python code.
Do not use Markdown code fences.
""",
        "tests": [
            ("binary_search([], 5)", -1),
            ("binary_search([1], 1)", 0),
            ("binary_search([1], 2)", -1),
            ("binary_search([1,3,5,7,9], 5)", 2),
            ("binary_search([1,3,5,7,9], 1)", 0),
            ("binary_search([1,3,5,7,9], 9)", 4),
            ("binary_search([1,3,5,7,9], 6)", -1),
        ]
    }
]