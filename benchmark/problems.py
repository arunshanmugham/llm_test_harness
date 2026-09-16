"""
problems.py

60-problem coding benchmark for comparing:
    F16
    Q6_K
    Q5_K_M
    Q4_K_M

Distribution:
    20 Easy
    20 Medium
    20 Hard

Each problem contains:
    name
    category
    prompt
    tests

Tests are intentionally NOT included in the model prompt.
"""


PROBLEMS = [

    # ========================================================
    # EASY 01
    # ========================================================

    {
        "name": "is_prime",
        "category": "easy",

        "prompt": """
Implement:

def is_prime(n):

Return True if n is prime, otherwise False.

Requirements:
- n < 2 is not prime.
- n is an integer.
- Do not use external libraries.

Return only the Python implementation.
""",

        "tests": [
            ("is_prime(-10)", False),
            ("is_prime(0)", False),
            ("is_prime(1)", False),
            ("is_prime(2)", True),
            ("is_prime(3)", True),
            ("is_prime(4)", False),
            ("is_prime(17)", True),
            ("is_prime(25)", False),
            ("is_prime(97)", True),
            ("is_prime(997)", True),
        ],
    },

    # ========================================================
    # EASY 02
    # ========================================================

    {
        "name": "factorial",
        "category": "easy",

        "prompt": """
Implement:

def factorial(n):

Return n factorial.

Requirements:
- n is a non-negative integer.
- factorial(0) must return 1.
- Do not use math.factorial.

Return only the Python implementation.
""",

        "tests": [
            ("factorial(0)", 1),
            ("factorial(1)", 1),
            ("factorial(2)", 2),
            ("factorial(5)", 120),
            ("factorial(8)", 40320),
            ("factorial(10)", 3628800),
        ],
    },

    # ========================================================
    # EASY 03
    # ========================================================

    {
        "name": "fibonacci",
        "category": "easy",

        "prompt": """
Implement:

def fibonacci(n):

Return the nth Fibonacci number.

Definition:
fibonacci(0) = 0
fibonacci(1) = 1

Requirements:
- n is a non-negative integer.

Return only the Python implementation.
""",

        "tests": [
            ("fibonacci(0)", 0),
            ("fibonacci(1)", 1),
            ("fibonacci(2)", 1),
            ("fibonacci(5)", 5),
            ("fibonacci(10)", 55),
            ("fibonacci(20)", 6765),
        ],
    },

    # ========================================================
    # EASY 04
    # ========================================================

    {
        "name": "reverse_string",
        "category": "easy",

        "prompt": """
Implement:

def reverse_string(text):

Return text with its characters reversed.

Return only the Python implementation.
""",

        "tests": [
            ("reverse_string('')", ""),
            ("reverse_string('a')", "a"),
            ("reverse_string('hello')", "olleh"),
            ("reverse_string('Python')", "nohtyP"),
            ("reverse_string('a b c')", "c b a"),
        ],
    },

    # ========================================================
    # EASY 05
    # ========================================================

    {
        "name": "palindrome",
        "category": "easy",

        "prompt": """
Implement:

def is_palindrome(text):

Return True if text is a palindrome.

Ignore:
- capitalization
- spaces
- punctuation

Only alphanumeric characters should be considered.

Return only the Python implementation.
""",

        "tests": [
            ("is_palindrome('')", True),
            ("is_palindrome('racecar')", True),
            ("is_palindrome('hello')", False),
            ("is_palindrome('RaceCar')", True),
            (
                "is_palindrome('A man, a plan, a canal: Panama!')",
                True,
            ),
            (
                "is_palindrome('Was it a car or a cat I saw?')",
                True,
            ),
            ("is_palindrome('OpenAI')", False),
        ],
    },

    # ========================================================
    # EASY 06
    # ========================================================

    {
        "name": "count_vowels",
        "category": "easy",

        "prompt": """
Implement:

def count_vowels(text):

Return the number of vowels in text.

Vowels are:
a, e, i, o, u

Counting must be case-insensitive.

Return only the Python implementation.
""",

        "tests": [
            ("count_vowels('')", 0),
            ("count_vowels('xyz')", 0),
            ("count_vowels('hello')", 2),
            ("count_vowels('AEIOU')", 5),
            ("count_vowels('Programming')", 3),
        ],
    },

    # ========================================================
    # EASY 07
    # ========================================================

    {
        "name": "find_max",
        "category": "easy",

        "prompt": """
Implement:

def find_max(values):

Return the largest number in a non-empty list.

Do not use max().

Return only the Python implementation.
""",

        "tests": [
            ("find_max([1])", 1),
            ("find_max([1,2,3])", 3),
            ("find_max([3,2,1])", 3),
            ("find_max([-5,-2,-10])", -2),
            ("find_max([7,7,7])", 7),
        ],
    },

    # ========================================================
    # EASY 08
    # ========================================================

    {
        "name": "remove_duplicates",
        "category": "easy",

        "prompt": """
Implement:

def remove_duplicates(values):

Return a new list with duplicates removed.

Requirements:
- Preserve the order of first occurrence.

Return only the Python implementation.
""",

        "tests": [
            ("remove_duplicates([])", []),
            ("remove_duplicates([1])", [1]),
            ("remove_duplicates([1,1,2,2,3])", [1,2,3]),
            ("remove_duplicates([3,1,3,2,1])", [3,1,2]),
            (
                "remove_duplicates(['a','b','a','c'])",
                ["a","b","c"],
            ),
        ],
    },

    # ========================================================
    # EASY 09
    # ========================================================

    {
        "name": "binary_search",
        "category": "easy",

        "prompt": """
Implement:

def binary_search(arr, target):

arr is sorted in ascending order.

Return the index of target.
Return -1 if target does not exist.

Requirements:
- Use binary search.
- Do not use list.index().

Return only the Python implementation.
""",

        "tests": [
            ("binary_search([],5)", -1),
            ("binary_search([1],1)", 0),
            ("binary_search([1],2)", -1),
            ("binary_search([1,3,5,7,9],1)", 0),
            ("binary_search([1,3,5,7,9],5)", 2),
            ("binary_search([1,3,5,7,9],9)", 4),
            ("binary_search([1,3,5,7,9],6)", -1),
        ],
    },

    # ========================================================
    # EASY 10
    # ========================================================

    {
        "name": "sum_digits",
        "category": "easy",

        "prompt": """
Implement:

def sum_digits(n):

Return the sum of the decimal digits of integer n.

Negative numbers should be treated as positive.

Return only the Python implementation.
""",

        "tests": [
            ("sum_digits(0)", 0),
            ("sum_digits(5)", 5),
            ("sum_digits(123)", 6),
            ("sum_digits(-123)", 6),
            ("sum_digits(9999)", 36),
        ],
    },

    # ========================================================
    # EASY 11
    # ========================================================

    {
        "name": "gcd",
        "category": "easy",

        "prompt": """
Implement:

def gcd(a, b):

Return the greatest common divisor of a and b.

Requirements:
- Support negative inputs.
- gcd(0, n) should return abs(n).
- Do not use math.gcd.

Return only the Python implementation.
""",

        "tests": [
            ("gcd(10,5)", 5),
            ("gcd(54,24)", 6),
            ("gcd(17,13)", 1),
            ("gcd(-54,24)", 6),
            ("gcd(0,5)", 5),
            ("gcd(5,0)", 5),
        ],
    },

    # ========================================================
    # EASY 12
    # ========================================================

    {
        "name": "word_count",
        "category": "easy",

        "prompt": """
Implement:

def word_count(text):

Return the number of whitespace-separated words.

Multiple spaces, tabs and newlines should not create
empty words.

Return only the Python implementation.
""",

        "tests": [
            ("word_count('')", 0),
            ("word_count('hello')", 1),
            ("word_count('hello world')", 2),
            ("word_count('  hello   world  ')", 2),
            ("word_count('one\\ntwo\\tthree')", 3),
        ],
    },

    # ========================================================
    # EASY 13
    # ========================================================

    {
        "name": "second_largest",
        "category": "easy",

        "prompt": """
Implement:

def second_largest(values):

Return the second largest DISTINCT number.

Return None if fewer than two distinct numbers exist.

Return only the Python implementation.
""",

        "tests": [
            ("second_largest([])", None),
            ("second_largest([1])", None),
            ("second_largest([1,1])", None),
            ("second_largest([1,2])", 1),
            ("second_largest([3,1,3,2])", 2),
            ("second_largest([-5,-1,-3])", -3),
        ],
    },

    # ========================================================
    # EASY 14
    # ========================================================

    {
        "name": "flatten_one_level",
        "category": "easy",

        "prompt": """
Implement:

def flatten_one_level(values):

values is a list of lists.

Return one flat list containing all elements in order.

Return only the Python implementation.
""",

        "tests": [
            ("flatten_one_level([])", []),
            ("flatten_one_level([[1,2],[3]])", [1,2,3]),
            ("flatten_one_level([[],[1],[]])", [1]),
            (
                "flatten_one_level([['a'],['b','c']])",
                ["a","b","c"],
            ),
        ],
    },

    # ========================================================
    # EASY 15
    # ========================================================

    {
        "name": "character_frequency",
        "category": "easy",

        "prompt": """
Implement:

def char_frequency(text):

Return a dictionary mapping every character to its
number of occurrences.

Characters are case-sensitive.

Return only the Python implementation.
""",

        "tests": [
            ("char_frequency('')", {}),
            ("char_frequency('a')", {"a": 1}),
            ("char_frequency('aab')", {"a": 2, "b": 1}),
            (
                "char_frequency('AaA')",
                {"A": 2, "a": 1},
            ),
        ],
    },

    # ========================================================
    # EASY 16
    # ========================================================

    {
        "name": "leap_year",
        "category": "easy",

        "prompt": """
Implement:

def is_leap_year(year):

Return True if year is a Gregorian leap year.

Rules:
- divisible by 400 -> leap year
- divisible by 100 -> not leap year
- divisible by 4 -> leap year

Return only the Python implementation.
""",

        "tests": [
            ("is_leap_year(2000)", True),
            ("is_leap_year(1900)", False),
            ("is_leap_year(2024)", True),
            ("is_leap_year(2023)", False),
            ("is_leap_year(2400)", True),
            ("is_leap_year(2100)", False),
        ],
    },

    # ========================================================
    # EASY 17
    # ========================================================

    {
        "name": "rotate_list",
        "category": "easy",

        "prompt": """
Implement:

def rotate_right(values, k):

Return a new list rotated right by k positions.

Requirements:
- k may be larger than the list length.
- Empty list returns [].
- Do not modify the input list.

Return only the Python implementation.
""",

        "tests": [
            ("rotate_right([],3)", []),
            ("rotate_right([1],10)", [1]),
            ("rotate_right([1,2,3,4,5],1)", [5,1,2,3,4]),
            ("rotate_right([1,2,3,4,5],2)", [4,5,1,2,3]),
            ("rotate_right([1,2,3],4)", [3,1,2]),
        ],
    },

    # ========================================================
    # EASY 18
    # ========================================================

    {
        "name": "common_elements",
        "category": "easy",

        "prompt": """
Implement:

def common_elements(a, b):

Return a list containing unique values that occur in both lists.

Requirements:
- Preserve their order of first appearance in a.
- Do not return duplicates.

Return only the Python implementation.
""",

        "tests": [
            ("common_elements([],[])", []),
            ("common_elements([1,2,3],[2,3,4])", [2,3]),
            ("common_elements([3,1,3,2],[3,2])", [3,2]),
            (
                "common_elements(['a','b','a'],['a'])",
                ["a"],
            ),
        ],
    },

    # ========================================================
    # EASY 19
    # ========================================================

    {
        "name": "run_length_encode",
        "category": "easy",

        "prompt": """
Implement:

def run_length_encode(text):

Compress consecutive repeated characters.

Return a list of (character, count) tuples.

Example:
"aaabbc" -> [('a',3), ('b',2), ('c',1)]

Return only the Python implementation.
""",

        "tests": [
            ("run_length_encode('')", []),
            ("run_length_encode('a')", [("a",1)]),
            (
                "run_length_encode('aaabbc')",
                [("a",3),("b",2),("c",1)],
            ),
            (
                "run_length_encode('aabbbaa')",
                [("a",2),("b",3),("a",2)],
            ),
        ],
    },

    # ========================================================
    # EASY 20
    # ========================================================

    {
        "name": "title_case_words",
        "category": "easy",

        "prompt": """
Implement:

def title_case_words(text):

Return a string where the first character of each
whitespace-separated word is uppercase and the remaining
characters are lowercase.

Output words must be separated by one space.

Return only the Python implementation.
""",

        "tests": [
            ("title_case_words('')", ""),
            ("title_case_words('hello world')", "Hello World"),
            ("title_case_words('HELLO WORLD')", "Hello World"),
            (
                "title_case_words('  python   CODING ')",
                "Python Coding",
            ),
        ],
    },


    # ========================================================
    # MEDIUM 01
    # ========================================================

    {
        "name": "merge_sort",
        "category": "medium",

        "prompt": """
Implement:

def merge_sort(arr):

Return a NEW list sorted in ascending order.

Requirements:
- Implement merge sort.
- Do not use sorted().
- Do not use list.sort().
- Support duplicates and negative numbers.

Return only the Python implementation.
""",

        "tests": [
            ("merge_sort([])", []),
            ("merge_sort([1])", [1]),
            ("merge_sort([3,1,2])", [1,2,3]),
            ("merge_sort([5,4,3,2,1])", [1,2,3,4,5]),
            ("merge_sort([3,3,1,2,1])", [1,1,2,3,3]),
            ("merge_sort([-5,2,-1,0,8])", [-5,-1,0,2,8]),
        ],
    },

    # ========================================================
    # MEDIUM 02
    # ========================================================

    {
        "name": "valid_parentheses",
        "category": "medium",

        "prompt": """
Implement:

def valid_parentheses(s):

Support (), [] and {}.

Return True only when all brackets are correctly
matched and nested.

Return only the Python implementation.
""",

        "tests": [
            ("valid_parentheses('')", True),
            ("valid_parentheses('()')", True),
            ("valid_parentheses('()[]{}')", True),
            ("valid_parentheses('(]')", False),
            ("valid_parentheses('([{}])')", True),
            ("valid_parentheses('([)]')", False),
            ("valid_parentheses('(((')", False),
            ("valid_parentheses('{[()()]}')", True),
        ],
    },

    # ========================================================
    # MEDIUM 03
    # ========================================================

    {
        "name": "group_anagrams",
        "category": "medium",

        "prompt": """
Implement:

def group_anagrams(words):

Group words that are anagrams.

Requirements:
- Return a list of lists.
- Preserve original word order inside each group.
- Preserve group order based on the first word that
  creates each group.
- Matching is case-sensitive.

Return only the Python implementation.
""",

        "tests": [
            (
                "group_anagrams(['eat','tea','tan','ate','nat','bat'])",
                [["eat","tea","ate"],["tan","nat"],["bat"]],
            ),
            ("group_anagrams([])", []),
            ("group_anagrams(['abc'])", [["abc"]]),
            (
                "group_anagrams(['ab','ba','abc','cab','bca'])",
                [["ab","ba"],["abc","cab","bca"]],
            ),
        ],
    },

    # ========================================================
    # MEDIUM 04
    # ========================================================

    {
        "name": "longest_common_prefix",
        "category": "medium",

        "prompt": """
Implement:

def longest_common_prefix(words):

Return the longest prefix shared by every string.

Return "" when there is no common prefix or the list is empty.

Return only the Python implementation.
""",

        "tests": [
            ("longest_common_prefix([])", ""),
            ("longest_common_prefix(['flower','flow','flight'])", "fl"),
            ("longest_common_prefix(['dog','racecar','car'])", ""),
            ("longest_common_prefix(['test'])", "test"),
            ("longest_common_prefix(['abc','abc','abc'])", "abc"),
        ],
    },

    # ========================================================
    # MEDIUM 05
    # ========================================================

    {
        "name": "two_sum_indices",
        "category": "medium",

        "prompt": """
Implement:

def two_sum(nums, target):

Return a tuple containing indices (i, j) where:
- i < j
- nums[i] + nums[j] == target

If multiple answers exist, return the pair with the smallest j;
if tied, the smallest i.

Return None if no pair exists.

Return only the Python implementation.
""",

        "tests": [
            ("two_sum([2,7,11,15],9)", (0,1)),
            ("two_sum([3,2,4],6)", (1,2)),
            ("two_sum([3,3],6)", (0,1)),
            ("two_sum([1,2,3],100)", None),
            ("two_sum([1,4,2,3],5)", (0,1)),
        ],
    },

    # ========================================================
    # MEDIUM 06
    # ========================================================

    {
        "name": "max_subarray",
        "category": "medium",

        "prompt": """
Implement:

def max_subarray_sum(nums):

Return the maximum sum of a contiguous non-empty subarray.

nums is non-empty.

Return only the Python implementation.
""",

        "tests": [
            ("max_subarray_sum([1])", 1),
            ("max_subarray_sum([-1])", -1),
            ("max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])", 6),
            ("max_subarray_sum([5,4,-1,7,8])", 23),
            ("max_subarray_sum([-5,-2,-8])", -2),
        ],
    },

    # ========================================================
    # MEDIUM 07
    # ========================================================

    {
        "name": "matrix_transpose",
        "category": "medium",

        "prompt": """
Implement:

def transpose(matrix):

Return the transpose of a rectangular matrix.

Requirements:
- [] returns [].
- Do not use numpy.

Return only the Python implementation.
""",

        "tests": [
            ("transpose([])", []),
            ("transpose([[1]])", [[1]]),
            ("transpose([[1,2],[3,4]])", [[1,3],[2,4]]),
            (
                "transpose([[1,2,3],[4,5,6]])",
                [[1,4],[2,5],[3,6]],
            ),
        ],
    },

    # ========================================================
    # MEDIUM 08
    # ========================================================

    {
        "name": "spiral_matrix",
        "category": "medium",

        "prompt": """
Implement:

def spiral_order(matrix):

Return all elements of a rectangular matrix in clockwise
spiral order starting at the top-left.

[] returns [].

Return only the Python implementation.
""",

        "tests": [
            ("spiral_order([])", []),
            ("spiral_order([[1]])", [1]),
            (
                "spiral_order([[1,2],[3,4]])",
                [1,2,4,3],
            ),
            (
                "spiral_order([[1,2,3],[4,5,6],[7,8,9]])",
                [1,2,3,6,9,8,7,4,5],
            ),
            (
                "spiral_order([[1,2,3,4],[5,6,7,8]])",
                [1,2,3,4,8,7,6,5],
            ),
        ],
    },

    # ========================================================
    # MEDIUM 09
    # ========================================================

    {
        "name": "deep_flatten",
        "category": "medium",

        "prompt": """
Implement:

def deep_flatten(values):

Recursively flatten arbitrarily nested Python lists.

Only lists should be recursively flattened.
Other values should remain unchanged.

Return only the Python implementation.
""",

        "tests": [
            ("deep_flatten([])", []),
            ("deep_flatten([1,2])", [1,2]),
            ("deep_flatten([1,[2,[3]],4])", [1,2,3,4]),
            (
                "deep_flatten([[['a']],['b',['c']]])",
                ["a","b","c"],
            ),
            (
                "deep_flatten([1,(2,3),[4]])",
                [1,(2,3),4],
            ),
        ],
    },

    # ========================================================
    # MEDIUM 10
    # ========================================================

    {
        "name": "roman_to_integer",
        "category": "medium",

        "prompt": """
Implement:

def roman_to_int(s):

Convert a valid Roman numeral to an integer.

Supported symbols:
I V X L C D M

Input is a valid Roman numeral in standard notation.

Return only the Python implementation.
""",

        "tests": [
            ("roman_to_int('I')", 1),
            ("roman_to_int('III')", 3),
            ("roman_to_int('IV')", 4),
            ("roman_to_int('IX')", 9),
            ("roman_to_int('LVIII')", 58),
            ("roman_to_int('MCMXCIV')", 1994),
        ],
    },

    # ========================================================
    # MEDIUM 11
    # ========================================================

    {
        "name": "integer_to_roman",
        "category": "medium",

        "prompt": """
Implement:

def int_to_roman(n):

Convert integer n to a Roman numeral.

Requirements:
- 1 <= n <= 3999
- Use standard subtractive Roman notation.

Return only the Python implementation.
""",

        "tests": [
            ("int_to_roman(1)", "I"),
            ("int_to_roman(4)", "IV"),
            ("int_to_roman(9)", "IX"),
            ("int_to_roman(58)", "LVIII"),
            ("int_to_roman(1994)", "MCMXCIV"),
            ("int_to_roman(3999)", "MMMCMXCIX"),
        ],
    },

    # ========================================================
    # MEDIUM 12
    # ========================================================

    {
        "name": "longest_unique_substring",
        "category": "medium",

        "prompt": """
Implement:

def longest_unique_substring_length(s):

Return the length of the longest substring containing
no repeated characters.

Return only the Python implementation.
""",

        "tests": [
            ("longest_unique_substring_length('')", 0),
            ("longest_unique_substring_length('abcabcbb')", 3),
            ("longest_unique_substring_length('bbbbb')", 1),
            ("longest_unique_substring_length('pwwkew')", 3),
            ("longest_unique_substring_length('abcdef')", 6),
            ("longest_unique_substring_length('abba')", 2),
        ],
    },

    # ========================================================
    # MEDIUM 13
    # ========================================================

    {
        "name": "product_except_self",
        "category": "medium",

        "prompt": """
Implement:

def product_except_self(nums):

Return a list where output[i] equals the product of all
nums elements except nums[i].

Requirements:
- Do not use division.
- O(n) time.
- Support zeros and negative numbers.

Return only the Python implementation.
""",

        "tests": [
            ("product_except_self([1,2,3,4])", [24,12,8,6]),
            ("product_except_self([-1,1,0,-3,3])", [0,0,9,0,0]),
            ("product_except_self([2,3])", [3,2]),
            ("product_except_self([0,0])", [0,0]),
        ],
    },

    # ========================================================
    # MEDIUM 14
    # ========================================================

    {
        "name": "merge_intervals",
        "category": "medium",

        "prompt": """
Implement:

def merge_intervals(intervals):

Each interval is [start, end].

Merge all overlapping OR touching intervals.

Return intervals sorted by start.

Do not modify the input.

Return only the Python implementation.
""",

        "tests": [
            ("merge_intervals([])", []),
            (
                "merge_intervals([[1,3],[2,6],[8,10],[15,18]])",
                [[1,6],[8,10],[15,18]],
            ),
            (
                "merge_intervals([[1,4],[4,5]])",
                [[1,5]],
            ),
            (
                "merge_intervals([[5,7],[1,2],[2,4]])",
                [[1,4],[5,7]],
            ),
        ],
    },

    # ========================================================
    # MEDIUM 15
    # ========================================================

    {
        "name": "top_k_frequent",
        "category": "medium",

        "prompt": """
Implement:

def top_k_frequent(nums, k):

Return the k most frequent distinct values.

Ordering:
1. Higher frequency first.
2. For equal frequency, smaller numeric value first.

Return only the Python implementation.
""",

        "tests": [
            ("top_k_frequent([1,1,1,2,2,3],2)", [1,2]),
            ("top_k_frequent([1],1)", [1]),
            (
                "top_k_frequent([4,4,1,1,2,2],2)",
                [1,2],
            ),
            (
                "top_k_frequent([-1,-1,2,2,2,3],2)",
                [2,-1],
            ),
        ],
    },

    # ========================================================
    # MEDIUM 16
    # ========================================================

    {
        "name": "evaluate_postfix",
        "category": "medium",

        "prompt": """
Implement:

def evaluate_postfix(tokens):

Evaluate a postfix expression.

tokens is a list of strings containing integers and:
+ - * /

Division must truncate toward zero.

Return the integer result.

Return only the Python implementation.
""",

        "tests": [
            ("evaluate_postfix(['2','1','+','3','*'])", 9),
            ("evaluate_postfix(['4','13','5','/','+'])", 6),
            (
                "evaluate_postfix(['10','6','9','3','+','-11','*','/','*','17','+','5','+'])",
                22,
            ),
            ("evaluate_postfix(['-7','3','/'])", -2),
        ],
    },

    # ========================================================
    # MEDIUM 17
    # ========================================================

    {
        "name": "word_frequency_sorted",
        "category": "medium",

        "prompt": """
Implement:

def word_frequency(text):

Return a list of (word, count) tuples.

Rules:
- Words are maximal sequences of letters or digits.
- Matching is case-insensitive.
- Sort by descending frequency.
- Break frequency ties alphabetically.

Use only the Python standard library.

Return only the Python implementation.
""",

        "tests": [
            ("word_frequency('')", []),
            (
                "word_frequency('Cat dog cat')",
                [("cat",2),("dog",1)],
            ),
            (
                "word_frequency('B b a A c')",
                [("a",2),("b",2),("c",1)],
            ),
            (
                "word_frequency('one, ONE! two?')",
                [("one",2),("two",1)],
            ),
        ],
    },

    # ========================================================
    # MEDIUM 18
    # ========================================================

    {
        "name": "nested_dictionary_get",
        "category": "medium",

        "prompt": """
Implement:

def nested_get(data, path, default=None):

path is a dot-separated string such as:
"user.address.city"

Walk nested dictionaries using each path component as a key.

Return default if any key is missing or if an intermediate
value is not a dictionary.

An empty path should return data.

Return only the Python implementation.
""",

        "tests": [
            ("nested_get({'a':{'b':2}},'a.b')", 2),
            ("nested_get({'a':{'b':2}},'a.c')", None),
            ("nested_get({'a':1},'a.b','missing')", "missing"),
            ("nested_get({'a':{'b':None}},'a.b','x')", None),
            ("nested_get({'a':1},'')", {"a":1}),
        ],
    },

    # ========================================================
    # MEDIUM 19
    # ========================================================

    {
        "name": "csv_summary",
        "category": "medium",

        "prompt": """
Implement:

def summarize_sales(rows):

rows is a list of dictionaries with:
{
    "product": str,
    "quantity": int,
    "price": float
}

Return a dictionary mapping each product to total revenue,
where revenue = quantity * price.

If the same product occurs multiple times, add the revenue.

Return only the Python implementation.
""",

        "tests": [
            ("summarize_sales([])", {}),
            (
                "summarize_sales([{'product':'A','quantity':2,'price':5.0}])",
                {"A":10.0},
            ),
            (
                "summarize_sales(["
                "{'product':'A','quantity':2,'price':5.0},"
                "{'product':'B','quantity':1,'price':3.0},"
                "{'product':'A','quantity':3,'price':2.0}"
                "])",
                {"A":16.0,"B":3.0},
            ),
        ],
    },

    # ========================================================
    # MEDIUM 20
    # ========================================================

    {
        "name": "dependency_order_simple",
        "category": "medium",

        "prompt": """
Implement:

def dependency_order(dependencies):

dependencies maps each task to a list of tasks that must
come BEFORE it.

Return a valid ordering containing every task appearing
either as a dictionary key or dependency.

Requirements:
- If several tasks are available at the same time,
  choose the alphabetically smallest.
- You may assume the graph has no cycle.

Return only the Python implementation.
""",

        "tests": [
            ("dependency_order({})", []),
            (
                "dependency_order({'build':['compile'],'compile':[]})",
                ["compile","build"],
            ),
            (
                "dependency_order({'c':['a','b'],'b':['a'],'a':[]})",
                ["a","b","c"],
            ),
            (
                "dependency_order({'deploy':['test'],'test':['build'],'build':[],'docs':[]})",
                ["build","docs","test","deploy"],
            ),
        ],
    },


    # ========================================================
    # HARD 01
    # ========================================================

    {
        "name": "lru_cache",
        "category": "hard",

        "prompt": """
Implement:

class LRUCache:

    def __init__(self, capacity):
        ...

    def get(self, key):
        ...

    def put(self, key, value):
        ...

Requirements:
- get returns -1 if key does not exist.
- get marks an existing key most recently used.
- put inserts or updates.
- Updating marks the key most recently used.
- When capacity is exceeded, evict the least recently used key.
- get and put must have O(1) average complexity.
- capacity is at least 1.

Return only the Python implementation.
""",

        "tests": [
            (
                "(lambda c:(c.put(1,1),c.get(1))[-1])(LRUCache(2))",
                1,
            ),
            (
                "(lambda c:(c.put(1,1),c.put(2,2),c.get(1),c.put(3,3),c.get(2))[-1])(LRUCache(2))",
                -1,
            ),
            (
                "(lambda c:(c.put(1,1),c.put(2,2),c.put(1,10),c.put(3,3),c.get(2))[-1])(LRUCache(2))",
                -1,
            ),
            (
                "(lambda c:(c.put(1,1),c.put(2,2),c.get(1),c.put(3,3),c.get(3))[-1])(LRUCache(2))",
                3,
            ),
        ],
    },

    # ========================================================
    # HARD 02
    # ========================================================

    {
        "name": "dijkstra_shortest_paths",
        "category": "hard",

        "prompt": """
Implement:

def dijkstra(graph, start):

graph is a dictionary:
node -> list of (neighbor, non_negative_weight)

Return a dictionary mapping every node appearing in graph
to its shortest distance from start.

Unreachable nodes must map to float('inf').

Return only the Python implementation.
""",

        "tests": [
            (
                "dijkstra({'A':[('B',1),('C',4)],'B':[('C',2)],'C':[]},'A')",
                {"A":0,"B":1,"C":3},
            ),
            (
                "dijkstra({'A':[('B',5)],'B':[],'C':[]},'A')",
                {"A":0,"B":5,"C":float("inf")},
            ),
            (
                "dijkstra({'A':[]},'A')",
                {"A":0},
            ),
        ],
    },

    # ========================================================
    # HARD 03
    # ========================================================

    {
        "name": "longest_common_subsequence",
        "category": "hard",

        "prompt": """
Implement:

def lcs_length(a, b):

Return the length of the longest common subsequence of
strings a and b.

Target complexity:
O(len(a) * len(b)) time.

Return only the Python implementation.
""",

        "tests": [
            ("lcs_length('','abc')", 0),
            ("lcs_length('abcde','ace')", 3),
            ("lcs_length('abc','abc')", 3),
            ("lcs_length('abc','def')", 0),
            ("lcs_length('AGGTAB','GXTXAYB')", 4),
            ("lcs_length('aaaa','aa')", 2),
        ],
    },

    # ========================================================
    # HARD 04
    # ========================================================

    {
        "name": "edit_distance",
        "category": "hard",

        "prompt": """
Implement:

def edit_distance(a, b):

Return the Levenshtein edit distance between strings a and b.

Allowed operations:
- insert one character
- delete one character
- replace one character

Each operation costs 1.

Return only the Python implementation.
""",

        "tests": [
            ("edit_distance('','')", 0),
            ("edit_distance('','abc')", 3),
            ("edit_distance('horse','ros')", 3),
            ("edit_distance('intention','execution')", 5),
            ("edit_distance('kitten','sitting')", 3),
            ("edit_distance('abc','abc')", 0),
        ],
    },

    # ========================================================
    # HARD 05
    # ========================================================

    {
        "name": "coin_change",
        "category": "hard",

        "prompt": """
Implement:

def coin_change(coins, amount):

Return the minimum number of coins required to make amount.

Return -1 if it is impossible.

Requirements:
- Each coin may be used unlimited times.
- amount >= 0.
- coin values are positive integers.

Return only the Python implementation.
""",

        "tests": [
            ("coin_change([1,2,5],11)", 3),
            ("coin_change([2],3)", -1),
            ("coin_change([1],0)", 0),
            ("coin_change([2,5,10,1],27)", 4),
            ("coin_change([3,7],14)", 2),
        ],
    },

    # ========================================================
    # HARD 06
    # ========================================================

    {
        "name": "minimum_path_sum",
        "category": "hard",

        "prompt": """
Implement:

def min_path_sum(grid):

grid is a non-empty rectangular matrix of non-negative integers.

Start at top-left and reach bottom-right.

You may move only:
- right
- down

Return the minimum possible sum including both endpoints.

Return only the Python implementation.
""",

        "tests": [
            ("min_path_sum([[1]])", 1),
            (
                "min_path_sum([[1,3,1],[1,5,1],[4,2,1]])",
                7,
            ),
            ("min_path_sum([[1,2,3],[4,5,6]])", 12),
            ("min_path_sum([[5],[1],[2]])", 8),
        ],
    },

    # ========================================================
    # HARD 07
    # ========================================================

    {
        "name": "number_of_islands",
        "category": "hard",

        "prompt": """
Implement:

def num_islands(grid):

grid is a rectangular list of lists containing:
'1' for land
'0' for water

An island is connected horizontally or vertically.

Return the number of islands.

Do not mutate the input grid.

Return only the Python implementation.
""",

        "tests": [
            ("num_islands([])", 0),
            ("num_islands([['1']])", 1),
            (
                "num_islands(["
                "['1','1','0','0'],"
                "['1','0','0','1'],"
                "['0','0','1','1']"
                "])",
                2,
            ),
            (
                "num_islands(["
                "['1','0','1'],"
                "['0','1','0'],"
                "['1','0','1']"
                "])",
                5,
            ),
        ],
    },

    # ========================================================
    # HARD 08
    # ========================================================

    {
        "name": "topological_sort_cycle",
        "category": "hard",

        "prompt": """
Implement:

def topological_sort(graph):

graph maps a node to a list of nodes it points to.

Return a topological ordering containing every node appearing
as either a key or neighbor.

Requirements:
- If several nodes have zero indegree, choose the
  alphabetically smallest.
- If the graph contains a cycle, return None.

Return only the Python implementation.
""",

        "tests": [
            ("topological_sort({})", []),
            (
                "topological_sort({'a':['b'],'b':['c'],'c':[]})",
                ["a","b","c"],
            ),
            (
                "topological_sort({'a':['c'],'b':['c'],'c':[]})",
                ["a","b","c"],
            ),
            (
                "topological_sort({'a':['b'],'b':['a']})",
                None,
            ),
        ],
    },

    # ========================================================
    # HARD 09
    # ========================================================

    {
        "name": "knapsack",
        "category": "hard",

        "prompt": """
Implement:

def knapsack(weights, values, capacity):

Solve the 0/1 knapsack problem.

Each item may be used at most once.

Return the maximum total value whose total weight does not
exceed capacity.

Return only the Python implementation.
""",

        "tests": [
            ("knapsack([],[],10)", 0),
            ("knapsack([1],[5],0)", 0),
            ("knapsack([1],[5],1)", 5),
            ("knapsack([1,3,4,5],[1,4,5,7],7)", 9),
            ("knapsack([10,20,30],[60,100,120],50)", 220),
        ],
    },

    # ========================================================
    # HARD 10
    # ========================================================

    {
        "name": "longest_increasing_subsequence",
        "category": "hard",

        "prompt": """
Implement:

def lis_length(nums):

Return the length of the longest strictly increasing
subsequence.

Target complexity:
O(n log n).

Return only the Python implementation.
""",

        "tests": [
            ("lis_length([])", 0),
            ("lis_length([1])", 1),
            ("lis_length([10,9,2,5,3,7,101,18])", 4),
            ("lis_length([0,1,0,3,2,3])", 4),
            ("lis_length([7,7,7,7])", 1),
            ("lis_length([1,2,3,4,5])", 5),
        ],
    },

    # ========================================================
    # HARD 11
    # ========================================================

    {
        "name": "word_break",
        "category": "hard",

        "prompt": """
Implement:

def word_break(s, words):

Return True if s can be segmented into one or more
dictionary words.

words is a list of non-empty strings.
Dictionary words may be reused.

The empty string is segmentable and should return True.

Return only the Python implementation.
""",

        "tests": [
            ("word_break('', ['a'])", True),
            ("word_break('leetcode',['leet','code'])", True),
            (
                "word_break('applepenapple',['apple','pen'])",
                True,
            ),
            (
                "word_break('catsandog',['cats','dog','sand','and','cat'])",
                False,
            ),
            (
                "word_break('aaaaaaa',['aaaa','aaa'])",
                True,
            ),
        ],
    },

    # ========================================================
    # HARD 12
    # ========================================================

    {
        "name": "decode_string",
        "category": "hard",

        "prompt": """
Implement:

def decode_string(s):

Decode strings encoded using:

k[encoded_string]

where encoded_string must be repeated k times.

Nested encodings are allowed.
k may contain multiple digits.

Examples:
3[a2[c]] -> accaccacc

Return only the Python implementation.
""",

        "tests": [
            ("decode_string('3[a]2[bc]')", "aaabcbc"),
            ("decode_string('3[a2[c]]')", "accaccacc"),
            ("decode_string('2[abc]3[cd]ef')", "abcabccdcdcdef"),
            ("decode_string('10[a]')", "aaaaaaaaaa"),
            ("decode_string('abc')", "abc"),
        ],
    },

    # ========================================================
    # HARD 13
    # ========================================================

    {
        "name": "basic_expression_evaluator",
        "category": "hard",

        "prompt": """
Implement:

def calculate(expression):

Evaluate an arithmetic expression containing:
- non-negative integer literals
- +
- -
- *
- /
- parentheses
- whitespace

Requirements:
- Normal operator precedence applies.
- Parentheses may be nested.
- Division truncates toward zero.
- Unary minus must be supported.
- Do not use eval(), exec(), compile(), ast.literal_eval(),
  or external libraries.

Return an integer.

Return only the Python implementation.
""",

        "tests": [
            ("calculate('1 + 2 * 3')", 7),
            ("calculate('(1 + 2) * 3')", 9),
            ("calculate('10 / 3')", 3),
            ("calculate('10 / -3')", -3),
            ("calculate('2*(5+5*2)/3+(6/2+8)')", 21),
            ("calculate('-(2+3)*4')", -20),
        ],
    },

    # ========================================================
    # HARD 14
    # ========================================================

    {
        "name": "json_diff",
        "category": "hard",

        "prompt": """
Implement:

def json_diff(a, b):

a and b contain nested dictionaries, lists and scalar values.

Return a list of string paths where values differ.

Rules:
- Dictionary keys use dot notation.
- List indices use [index].
- Missing dictionary keys count as differences.
- Missing list positions count as differences.
- Return paths sorted lexicographically.
- If the root scalar values differ, use path "$".

Example:
{"user":{"age":20}} vs {"user":{"age":21}}
returns ["user.age"]

Return only the Python implementation.
""",

        "tests": [
            ("json_diff({'a':1},{'a':1})", []),
            ("json_diff({'a':1},{'a':2})", ["a"]),
            (
                "json_diff({'a':{'b':1}},{'a':{'b':2}})",
                ["a.b"],
            ),
            (
                "json_diff({'a':[1,2]},{'a':[1,3,4]})",
                ["a[1]","a[2]"],
            ),
            (
                "json_diff({'a':1},{'b':1})",
                ["a","b"],
            ),
            ("json_diff(1,2)", ["$"]),
        ],
    },

    # ========================================================
    # HARD 15
    # ========================================================

    {
        "name": "rate_limiter",
        "category": "hard",

        "prompt": """
Implement:

class RateLimiter:

    def __init__(self, limit, window):
        ...

    def allow(self, user, timestamp):
        ...

Implement a per-user sliding-window rate limiter.

Requirements:
- limit is the maximum number of allowed requests in window
  seconds.
- timestamp is an integer and calls arrive in non-decreasing
  timestamp order.
- A previous allowed request at time t remains in the window
  when timestamp - t < window.
- Rejected requests must NOT be recorded.
- Different users have independent limits.
- allow returns True when accepted, otherwise False.

Return only the Python implementation.
""",

        "tests": [
            (
                "(lambda r:[r.allow('a',0),r.allow('a',1),r.allow('a',2)])(RateLimiter(2,10))",
                [True,True,False],
            ),
            (
                "(lambda r:[r.allow('a',0),r.allow('a',1),r.allow('a',10)])(RateLimiter(2,10))",
                [True,True,True],
            ),
            (
                "(lambda r:[r.allow('a',0),r.allow('b',0),r.allow('a',1),r.allow('b',1)])(RateLimiter(1,10))",
                [True,True,False,False],
            ),
            (
                "(lambda r:[r.allow('a',0),r.allow('a',1),r.allow('a',2),r.allow('a',10),r.allow('a',11)])(RateLimiter(2,10))",
                [True,True,False,True,True],
            ),
        ],
    },

    # ========================================================
    # HARD 16
    # ========================================================

    {
        "name": "dependency_resolver",
        "category": "hard",

        "prompt": """
Implement:

def resolve_dependencies(dependencies, targets):

dependencies maps package -> list of packages it depends on.

Return an installation order containing:
- every target
- all transitive dependencies of every target

Requirements:
- Dependencies must appear before packages that need them.
- Include each package exactly once.
- If multiple packages are currently eligible, choose the
  alphabetically smallest.
- Packages mentioned only as dependencies must still be included.
- If a cycle exists in the required dependency subgraph,
  return None.

Return only the Python implementation.
""",

        "tests": [
            (
                "resolve_dependencies({'app':['db'],'db':[]},['app'])",
                ["db","app"],
            ),
            (
                "resolve_dependencies({'app':['api','db'],'api':['core'],'db':['core'],'core':[]},['app'])",
                ["core","api","db","app"],
            ),
            (
                "resolve_dependencies({'a':['b'],'b':['a']},['a'])",
                None,
            ),
            (
                "resolve_dependencies({'a':['x'],'b':['y']},['b'])",
                ["y","b"],
            ),
        ],
    },

    # ========================================================
    # HARD 17
    # ========================================================

    {
        "name": "shortest_word_ladder",
        "category": "hard",

        "prompt": """
Implement:

def word_ladder_length(begin, end, words):

Return the number of words in the shortest transformation
sequence from begin to end.

Rules:
- Change exactly one character per step.
- Every transformed word except begin must occur in words.
- All words have equal length.
- Return 0 if no transformation exists.
- If begin == end, return 1.

Example:
hit -> hot -> dot -> dog -> cog
has length 5.

Return only the Python implementation.
""",

        "tests": [
            (
                "word_ladder_length('hit','cog',['hot','dot','dog','lot','log','cog'])",
                5,
            ),
            (
                "word_ladder_length('hit','cog',['hot','dot','dog','lot','log'])",
                0,
            ),
            (
                "word_ladder_length('a','c',['a','b','c'])",
                2,
            ),
            (
                "word_ladder_length('same','same',['same'])",
                1,
            ),
        ],
    },

    # ========================================================
    # HARD 18
    # ========================================================

    {
        "name": "task_scheduler",
        "category": "hard",

        "prompt": """
Implement:

def min_schedule_time(tasks, cooldown):

Each item in tasks is a task identifier.

Every task takes one time unit.

Two executions of the SAME task must have at least
cooldown time units between them.

Different tasks may run in any order.
Idle time is allowed.

Return the minimum total number of time units needed
to execute all tasks.

Return only the Python implementation.
""",

        "tests": [
            ("min_schedule_time([],2)", 0),
            ("min_schedule_time(['A'],2)", 1),
            (
                "min_schedule_time(['A','A','A','B','B','B'],2)",
                8,
            ),
            (
                "min_schedule_time(['A','A','A','B','B','B'],0)",
                6,
            ),
            (
                "min_schedule_time(['A','A','A','A','B','B','C','C'],2)",
                10,
            ),
        ],
    },

    # ========================================================
    # HARD 19
    # ========================================================

    {
        "name": "wildcard_matching",
        "category": "hard",

        "prompt": """
Implement:

def wildcard_match(text, pattern):

Pattern rules:
- ? matches exactly one character.
- * matches any sequence of characters, including empty.
- All other characters match themselves.

The entire text must match the entire pattern.

Return True or False.

Return only the Python implementation.
""",

        "tests": [
            ("wildcard_match('aa','a')", False),
            ("wildcard_match('aa','*')", True),
            ("wildcard_match('cb','?a')", False),
            ("wildcard_match('adceb','*a*b')", True),
            ("wildcard_match('acdcb','a*c?b')", False),
            ("wildcard_match('','*')", True),
            ("wildcard_match('','?')", False),
        ],
    },

    # ========================================================
    # HARD 20
    # ========================================================

    {
        "name": "transaction_reconciliation",
        "category": "hard",

        "prompt": """
Implement:

def reconcile_transactions(expected, actual):

expected and actual are lists of dictionaries:

{
    "id": str,
    "amount": number,
    "currency": str
}

Transaction ids are unique within each list.

Return a dictionary:

{
    "missing": [...],
    "unexpected": [...],
    "mismatched": [...]
}

Definitions:
- missing: ids present in expected but absent from actual
- unexpected: ids present in actual but absent from expected
- mismatched: ids present in both where amount OR currency differs

Requirements:
- Each returned list contains transaction ids only.
- Sort every returned list lexicographically by id.
- Numeric amounts compare using normal Python numeric equality.

Return only the Python implementation.
""",

        "tests": [
            (
                "reconcile_transactions([],[])",
                {
                    "missing": [],
                    "unexpected": [],
                    "mismatched": [],
                },
            ),
            (
                "reconcile_transactions("
                "[{'id':'1','amount':10,'currency':'USD'}],"
                "[{'id':'1','amount':10,'currency':'USD'}]"
                ")",
                {
                    "missing": [],
                    "unexpected": [],
                    "mismatched": [],
                },
            ),
            (
                "reconcile_transactions("
                "[{'id':'1','amount':10,'currency':'USD'},"
                "{'id':'2','amount':20,'currency':'USD'}],"
                "[{'id':'1','amount':11,'currency':'USD'},"
                "{'id':'3','amount':20,'currency':'USD'}]"
                ")",
                {
                    "missing": ["2"],
                    "unexpected": ["3"],
                    "mismatched": ["1"],
                },
            ),
            (
                "reconcile_transactions("
                "[{'id':'b','amount':1,'currency':'USD'},"
                "{'id':'a','amount':2,'currency':'EUR'}],"
                "[{'id':'a','amount':2,'currency':'USD'},"
                "{'id':'c','amount':3,'currency':'USD'}]"
                ")",
                {
                    "missing": ["b"],
                    "unexpected": ["c"],
                    "mismatched": ["a"],
                },
            ),
        ],
    },
]