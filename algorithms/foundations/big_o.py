"""
Big O Notation — Complexity Examples
=====================================

Big O notation describes the upper bound of an algorithm's growth rate.
It tells us how runtime or memory scales as input size (n) grows.

Common complexities (from fastest to slowest):
    O(1)        — Constant
    O(log n)    — Logarithmic
    O(n)        — Linear
    O(n log n)  — Linearithmic
    O(n²)       — Quadratic
    O(2^n)      — Exponential
    O(n!)       — Factorial
"""

from typing import List


# ──────────────────────────────────────────────
# O(1) — Constant Time
# ──────────────────────────────────────────────
def constant_time_example(arr: List[int]) -> int:
    """
    Access the first element of an array.
    No matter how large the array is, this takes the same time.

    Time Complexity:  O(1)
    Space Complexity: O(1)

    Real-world example: Looking up a value in a hash map by key.
    """
    # Step 1: Directly access index 0 — single operation
    return arr[0] if arr else -1


# ──────────────────────────────────────────────
# O(log n) — Logarithmic Time
# ──────────────────────────────────────────────
def logarithmic_time_example(arr: List[int], target: int) -> int:
    """
    Binary search — halves the search space each iteration.

    Time Complexity:  O(log n)
    Space Complexity: O(1)

    Real-world example: Looking up a word in a dictionary.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        # Step 1: Find the middle index
        mid = (left + right) // 2

        # Step 2: Compare middle element with target
        if arr[mid] == target:
            return mid       # Found it!
        elif arr[mid] < target:
            left = mid + 1   # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found


# ──────────────────────────────────────────────
# O(n) — Linear Time
# ──────────────────────────────────────────────
def linear_time_example(arr: List[int]) -> int:
    """
    Find the maximum element by scanning every element once.

    Time Complexity:  O(n)
    Space Complexity: O(1)

    Real-world example: Finding the tallest person in a line.
    """
    if not arr:
        return -1

    max_val = arr[0]

    # Step 1: Visit each element exactly once
    for num in arr:
        # Step 2: Update max if current element is larger
        if num > max_val:
            max_val = num

    return max_val


# ──────────────────────────────────────────────
# O(n log n) — Linearithmic Time
# ──────────────────────────────────────────────
def linearithmic_time_example(arr: List[int]) -> List[int]:
    """
    Merge sort — divides array in half (log n levels), merges each level (n work).

    Time Complexity:  O(n log n)
    Space Complexity: O(n)

    Real-world example: Sorting a deck of cards using merge sort.
    """
    if len(arr) <= 1:
        return arr

    # Step 1: Split the array in half
    mid = len(arr) // 2
    left = linearithmic_time_example(arr[:mid])
    right = linearithmic_time_example(arr[mid:])

    # Step 2: Merge the two sorted halves
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays into one sorted array."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ──────────────────────────────────────────────
# O(n²) — Quadratic Time
# ──────────────────────────────────────────────
def quadratic_time_example(arr: List[int]) -> List[tuple]:
    """
    Find all pairs in an array — two nested loops.

    Time Complexity:  O(n²)
    Space Complexity: O(n²) for storing pairs

    Real-world example: Comparing every student with every other student.
    """
    pairs = []

    # Step 1: Outer loop — pick first element
    for i in range(len(arr)):
        # Step 2: Inner loop — pick second element
        for j in range(i + 1, len(arr)):
            # Step 3: Record the pair
            pairs.append((arr[i], arr[j]))

    return pairs


# ──────────────────────────────────────────────
# O(2^n) — Exponential Time
# ──────────────────────────────────────────────
def exponential_time_example(n: int) -> int:
    """
    Naive recursive Fibonacci — each call spawns two more calls.

    Time Complexity:  O(2^n)
    Space Complexity: O(n) — recursion stack depth

    Real-world example: Brute-force solving all subsets of a set.
    """
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Step 1: Recursively compute fib(n-1) + fib(n-2)
    # This creates an exponentially growing call tree
    return exponential_time_example(n - 1) + exponential_time_example(n - 2)


# ──────────────────────────────────────────────
# Complexity comparison helper
# ──────────────────────────────────────────────
COMPLEXITY_TABLE = {
    "O(1)": {
        "name": "Constant",
        "description": "Same time regardless of input size",
        "example": "Array index access, hash table lookup",
        "growth": [1, 1, 1, 1, 1],
    },
    "O(log n)": {
        "name": "Logarithmic",
        "description": "Halves the problem each step",
        "example": "Binary search, balanced BST operations",
        "growth": [1, 2, 3, 4, 5],  # log2(2), log2(4), ..., log2(32)
    },
    "O(n)": {
        "name": "Linear",
        "description": "Grows proportionally to input",
        "example": "Linear search, array traversal",
        "growth": [2, 4, 8, 16, 32],
    },
    "O(n log n)": {
        "name": "Linearithmic",
        "description": "Slightly worse than linear",
        "example": "Merge sort, heap sort",
        "growth": [2, 8, 24, 64, 160],
    },
    "O(n²)": {
        "name": "Quadratic",
        "description": "Nested iterations over input",
        "example": "Bubble sort, selection sort",
        "growth": [4, 16, 64, 256, 1024],
    },
    "O(2^n)": {
        "name": "Exponential",
        "description": "Doubles with each additional input",
        "example": "Recursive Fibonacci, power set",
        "growth": [4, 16, 256, 65536, 4294967296],
    },
}
