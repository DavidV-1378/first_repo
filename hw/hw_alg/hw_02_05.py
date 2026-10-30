# H1/BO2
# 1) n represents the temperature values in the list.
# temperature = [22.5, 20.0, 23.5], n = 3
# 2) n represents the lenght of the string.
# "python", n = 6
# 3) n reprents the number of usernames in the list. q is the number of queries.
# usernames = ["name1", "name2", "name3"], n = 3
# queries = ["name1", "name4"], q = 2

# H2/BO2
# 0: 0 checks, 1: 1 checks, 2: 2 checks, 5: 5 checks, 10: 10 chekcs;
# Because the target is missing from the list, a linear search will go through all the list.
# Therefore the number of checks is always equal to the lenght of the list.
# Growth classification: linear growth
# Notation: O(n)
# The counted operation is the equality check.

# H3/BO2
# 1) Retrieve and return `values[0]`, with a non-empty-input contract.
# Counted Operation: Array index lookup / element retrieval (`values[0]`).
# Counts Table:
# n = 1: 1 lookup
# n = 2: 1 lookup
# n = 4: 1 lookup
#
# Growth Classification: Constant 
#
# Explanation: As n grows from 1 to 4, the operation count stays fixed at 1.
# Because the count is independent of the input size the growth is constant.


# 2) Visit every value once in a single loop.
# Counted Operation: Element visitation / iteration step.
# Counts Table:
# n = 1: 1 visit
# n = 2: 2 visits
# n = 4: 4 visits
#
# Growth Classification: Linear 
#
# Explanation: Doubling n directly doubles the operation count (from 1 to 2, 
# and 2 to 4). Since the number of operations scales directly proportional 
# to n, the growth is linear.


# 3) Visit every ordered pair using two full nested loops over the list.
# Counted Operation: Pair visitation / inner-loop step.
# Counts Table:
# n = 1: 1 pair visit  
# n = 2: 4 pair visits
# n = 4: 16 pair visits
# 
# Growth Classification: Quadratic 
# 
# Explanation: Doubling the input size n increases the operation count by a 
# factor of 4 (2^2). Since the count scales proportional to n^2, the growth 
# is quadratic.

# H4/BO2
# Best-case scenario:
# Input list: [10, 20, 30, 40, 50]
# Target: 10
# Equality checks: 1
# Explanation: The target is found at the very first index, so the 
# linear search stops after 1 comparison.


# Worst-case scenario:
# Input list: [10, 20, 30, 40, 50]
# Target: 50
# Equality checks: 5
# Explanation: The target is located at the end of the list, requiring 
# the search to check every single item in the list.

# Explenation: Lists of the same lenght can require different amount of work because
# the amount of chekcs depends on where the target is located. 

# H5/BO2

def has_duplicate_slow(items: list[int]) -> bool:
    n = len(items)
    for first_index in range(n):
        for second_index in range(first_index + 1, n):
            if items[first_index] == items[second_index]:
                return True
    return False


def has_duplicate_seen(items: list[int]) -> bool:
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

empty_list = []
unique_list = [1, 2, 3, 4, 5]
early_duplicate_list = [7, 7, 1, 2, 3]
late_duplicate_list = [1, 2, 3, 4, 1]

assert has_duplicate_seen([]) == False
assert has_duplicate_seen([42]) == False
assert has_duplicate_seen([10, 20]) == False
assert has_duplicate_seen([5, 12, 5]) == True
assert has_duplicate_seen([-3, -10, -3]) == True
assert has_duplicate_seen([-1, -2, -3]) == False
assert has_duplicate_seen([1, 8, 3, 14, 9]) == False

# State meanings explenation:
# 1) seen:
# Stores all unique values visited so far from left to right.
# 2) item: 
# The current value being inspected in the loop iteration.
# 3) Return Value:
# True if a duplicate item is detected, or False if the full list is checked with no duplicates found.

# H6/BO2

# Contract & Behavior Decisions
# Both functions return a list of booleans matching the order of query_ids.
# Empty inputs (empty products or queries) return valid lists without error.

# Examples pre coding
# Example 1: Products = [101, 102], Queries = [102, 999] -> [True, False]
# Example 2: Products = [], Queries = [101] -> [False]

# n and q meanings:
# n is the number of product IDs in the catalog.
# q is the number of query IDs to look up.
#
# Simpler approach for one query:
# Repeated linear search against the original list is simpler because it requires 
# no setup work or extra data structures.
#
# Better suited approach for many queries:
# The set-based approach is better suited for many queries because lookup time in a set 
# is O(1) on average, yielding O(n + q) total work versus O(n * q) for list search.
#
# Additional state stored in set-based approach:
# It stores a set data structure containing all unique product IDs from the original list.
#
# Setup work versus query work:
# List approach: O(1) setup work, O(n) work per query.
# Set approach: O(n) setup work to build the set, O(1) work per query.


def lookup_products_list(product_ids: list[int], query_ids: list[int]) -> list[bool]:
    results = []
    for q_id in query_ids:
        results.append(q_id in product_ids)
    return results


def lookup_products_set(product_ids: list[int], query_ids: list[int]) -> list[bool]:
    product_set = set(product_ids)
    results = []
    for q_id in query_ids:
        results.append(q_id in product_set)
    return results

# Tests:

assert lookup_products_list([101, 102, 103], [102, 999]) == [True, False]
assert lookup_products_set([101, 102, 103], [102, 999]) == [True, False]

assert lookup_products_list([], [101, 102]) == [False, False]
assert lookup_products_set([], [101, 102]) == [False, False]

assert lookup_products_list([101, 102], []) == []
assert lookup_products_set([101, 102], []) == []

assert lookup_products_list([101, 102], [101, 101, 999, 101]) == [True, True, False, True]
assert lookup_products_set([101, 102], [101, 101, 999, 101]) == [True, True, False, True]

assert lookup_products_list([101, 101, 102], [101, 102, 103]) == [True, True, False]
assert lookup_products_set([101, 101, 102], [101, 102, 103]) == [True, True, False]

# H1/BO4

# prefix[k] represents the sum of the first k elements of the array.
# By convention, prefix[0] = 0.

# Original Array: [3, -2, 5, 0, 4]
#
# Boundary Label (k)  Array Elements Included    Calculation    prefix[k]
#         0                   None                     0              0
#         1                   [3]                    0 + 3            3
#         2                 [3, -2]                 3 + (-2)          1
#         3                [3, -2, 5]                1 + 5            6
#         4               [3, -2, 5, 0]              6 + 0            6
#         5              [3, -2, 5, 0, 4]            6 + 4            10
#
# Completed Prefix Table: [0, 3, 1, 6, 6, 10]


# Range Query Calculations using prefix[right] - prefix[left]
# Range [left, right) uses elements from index left up to right - 1.

# 1) Range [0, 2)
# Prediction: 3 + (-2) = 1
# prefix[2] - prefix[0] = 1 - 0 = 1

# 2) Range [1, 4)
# Prediction: (-2) + 5 + 0 = 3
# prefix[4] - prefix[1] = 6 - 3 = 3

# 3) Range [2, 5)
# Prediction: 5 + 0 + 4 = 9
# prefix[5] - prefix[2] = 10 - 1 = 9

# 4) Range [4, 4)
# Prediction: Empty range = 0
# prefix[4] - prefix[4] = 6 - 6 = 0

# H2/B04

# Contract & Behavior Decisions
# Invalid-range behavior:
# If left > right, left < 0, or right > length of the list, query_even_count
# raises a ValueError.
#
# Empty-input behavior:
# An empty list creates a prefix table [0]. Any valid range on an empty list
# (e.g., [0, 0)) returns 0.

# Input List: [2, 3, 0, -4, 5], Length = 5
# Example 1 (Full range [0, 5)): Even values are 2, 0, -4 -> count is 3
# Example 2 (Single item [1, 2)): Element is 3 (odd) -> count is 0

# Efficiency:
# Preprocessing Time: O(n) to iterate over the array once and build the prefix table.
# Query Time: O(1) to perform a single subtraction lookup (even_prefix[right] - even_prefix[left]).
# Extra Space: O(n) auxiliary space to store the prefix count array of size n + 1.

def build_even_prefix(numbers: list[int]) -> list[int]:
    """Preprocesses list to create prefix sum array of even value counts."""
    prefix = [0] * (len(numbers) + 1)
    for i in range(len(numbers)):
        is_even = 1 if numbers[i] % 2 == 0 else 0
        prefix[i + 1] = prefix[i] + is_even
    return prefix


def query_even_count(prefix: list[int], left: int, right: int) -> int:
    """Returns number of even values in half-open range [left, right)."""
    if left < 0 or right >= len(prefix) or left > right:
        raise ValueError("Invalid range indices.")
    return prefix[right] - prefix[left]

# Automated Tests

numbers = [2, 3, 0, -4, 5]
prefix = build_even_prefix(numbers)

assert query_even_count(prefix, 0, 5) == 3

assert query_even_count(prefix, 2, 3) == 1

assert query_even_count(prefix, 1, 2) == 0

assert query_even_count(prefix, 3, 3) == 0

assert query_even_count(prefix, 2, 4) == 2

empty_prefix = build_even_prefix([])
assert query_even_count(empty_prefix, 0, 0) == 0

try:
    query_even_count(prefix, 3, 2)
    assert False
except ValueError:
    pass

try:
    query_even_count(prefix, -1, 3)
    assert False
except ValueError:
    pass

try:
    query_even_count(prefix, 0, 10)
    assert False
except ValueError:
    pass

# H3/BO4

# Vowel set: 'a', 'e', 'i', 'o', 'u' (case-insensitive, including uppercase 'A', 'E', 'I', 'O', 'U').
# Invalid ranges (start < 0, end > length, or start > end) raise a ValueError.
# Empty input string creates a prefix table [0]. Any valid range on empty text returns 0.

# Text = "Hello, World!"
# Example 1: text[0:5] -> "Hello" has vowels 'e', 'o' -> count is 2
# Example 2: text[7:12] -> "World" has vowel 'o' -> count is 1

# Efficiency:
# Preprocessing Cost: O(n) time to iterate over string length n and O(n) space for the prefix array.
# Per-Query Cost: O(1) time using a single lookup subtraction (vowel_prefix[end] - vowel_prefix[start]).


# Implementation

def build_vowel_prefix(text: str) -> list[int]:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    prefix = [0] * (len(text) + 1)
    for i, char in enumerate(text):
        is_vowel = 1 if char in vowels else 0
        prefix[i + 1] = prefix[i] + is_vowel
    return prefix


def query_vowel_count(prefix: list[int], start: int, end: int) -> int:
    if start < 0 or end >= len(prefix) or start > end:
        raise ValueError("Invalid range indices.")
    return prefix[end] - prefix[start]

# Tests

text = "Hello, World!"
prefix = build_vowel_prefix(text)

assert query_vowel_count(prefix, 0, 5) == 2

assert query_vowel_count(prefix, 5, 7) == 0

assert query_vowel_count(build_vowel_prefix("fly kyz"), 0, 7) == 0

assert query_vowel_count(prefix, 3, 3) == 0

assert query_vowel_count(prefix, 0, len(text)) == 3

empty_prefix = build_vowel_prefix("")
assert query_vowel_count(empty_prefix, 0, 0) == 0

try:
    query_vowel_count(prefix, 4, 2)
    assert False
except ValueError:
    pass

try:
    query_vowel_count(prefix, -1, 3)
    assert False
except ValueError:
    pass

# H4/BO5

# Contract & Behavior Decisions
# Range sums use half-open intervals [left, right).
# Invalid range bounds raise a ValueError.

# 1-2 Concrete Examples (before coding)
# Input List: [1, 2, 3, 4, 5], Query [1, 4)
# Direct: 2 + 3 + 4 = 9
# Prefix: prefix[4] - prefix[1] = 10 - 1 = 9

# Short Explanation: Time/Memory Tradeoff & Preprocessing Justification
# Record Setup:
# n = 10,000 
# q = 5,000
#
# Operation Counts Recorded:
# Prefix construction work: 10,000 additions (O(n)).
# Direct queries work: ~25,000,000 additions (O(q * n)).
# Prefix queries work: 5,000 subtractions (O(q)).
#
# Direct approach uses O(1) auxiliary space but takes O(k) additions per query,
# resulting in O(q * n) total work for many queries.
# Prefix approach uses O(n) extra space to store the prefix array, but reduces
# query work to O(1) subtraction per query, yielding O(n + q) total work.
#
# Preprocessing is justified when q is large, many queries over the same data
# or when real-time, low-latency query responses are required. If q is very small, 
# direct summation is better because building the prefix table overhead isn't worth it.

def direct_range_sum(numbers: list[int], left: int, right: int) -> int:
    """Computes range sum directly by slicing/iterating over the array."""
    if left < 0 or right > len(numbers) or left > right:
        raise ValueError("Invalid range indices.")
    return sum(numbers[left:right])


def build_prefix_sum(numbers: list[int]) -> list[int]:
    """Preprocesses list to construct a prefix sum array."""
    prefix = [0] * (len(numbers) + 1)
    for i, val in enumerate(numbers):
        prefix[i + 1] = prefix[i] + val
    return prefix


def prefix_range_sum(prefix: list[int], left: int, right: int) -> int:
    """Computes range sum in O(1) using precalculated prefix array."""
    if left < 0 or right >= len(prefix) or left > right:
        raise ValueError("Invalid range indices.")
    return prefix[right] - prefix[left]


n = 10000
q = 5000

numbers = list(range(n))

queries = []
for i in range(q):
    left = (i * 37) % (n - 1)
    right = left + 1 + ((i * 53) % (n - left))
    queries.append((left, right))


prefix = build_prefix_sum(numbers)
prefix_construction_ops = len(numbers)

direct_results = []
direct_ops = 0
for l, r in queries:
    direct_results.append(direct_range_sum(numbers, l, r))
    direct_ops += max(0, r - l - 1)

prefix_results = []
prefix_ops = 0
for l, r in queries:
    prefix_results.append(prefix_range_sum(prefix, l, r))
    prefix_ops += 1

assert direct_results == prefix_results

print(f"n = {n}, q = {q}")
print(f"Prefix Construction Operations: {prefix_construction_ops:,} additions")
print(f"Direct Queries Operations:       {direct_ops:,} additions")
print(f"Prefix Queries Operations:       {prefix_ops:,} subtractions")


# Edge Case Tests

test_nums = [1, 2, 3, 4, 5]
test_prefix = build_prefix_sum(test_nums)

assert direct_range_sum(test_nums, 1, 2) == prefix_range_sum(test_prefix, 1, 2) == 2

assert direct_range_sum(test_nums, 2, 2) == prefix_range_sum(test_prefix, 2, 2) == 0

assert direct_range_sum(test_nums, 0, 5) == prefix_range_sum(test_prefix, 0, 5) == 15