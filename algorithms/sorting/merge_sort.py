"""
Merge Sort
===========

A divide-and-conquer sorting algorithm that splits the array in half,
recursively sorts each half, then merges them back together.

Time Complexity:  O(n log n) always
Space Complexity: O(n) — needs auxiliary space for merging

Real-world: Used in external sorting (sorting data that doesn't fit in memory).
            Stable sort — preserves relative order of equal elements.
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """
    Sort using merge sort.

    Steps:
        1. Base case: arrays of length 0 or 1 are already sorted
        2. Split the array into two halves
        3. Recursively sort each half
        4. Merge the two sorted halves
    """
    # Step 1: Base case
    if len(arr) <= 1:
        return arr

    # Step 2: Split in half
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Step 4: Merge sorted halves
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted arrays into one sorted array.

    Uses two pointers — one for each array.
    Compare elements at both pointers, take the smaller one.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_traced(arr: List[int]) -> dict:
    """Merge sort with step trace for visualization."""
    steps = [{"type": "initial", "array": list(arr)}]

    def _sort(arr, depth=0):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        steps.append({"type": "split", "array": list(arr), "mid": mid, "depth": depth})

        left = _sort(arr[:mid], depth + 1)
        right = _sort(arr[mid:], depth + 1)

        merged = _merge(left, right)
        steps.append({"type": "merge", "left": list(left), "right": list(right),
                       "result": list(merged), "depth": depth})
        return merged

    sorted_arr = _sort(arr)
    steps.append({"type": "done", "array": sorted_arr})
    return {"sorted": sorted_arr, "steps": steps}
