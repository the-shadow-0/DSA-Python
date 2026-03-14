"""
Binary Search
==============

Efficiently searches a SORTED array by repeatedly halving the search space.

Time Complexity:  O(log n)
Space Complexity: O(1) iterative, O(log n) recursive

Real-world: Dictionary lookup, finding a page in a book, database index search.
"""

from typing import List


def binary_search(arr: List[int], target: int) -> int:
    """
    Iterative binary search. Array must be sorted.

    Steps:
        1. Set left and right boundaries
        2. Find the middle element
        3. If middle == target → found!
        4. If target < middle → search left half
        5. If target > middle → search right half
        6. Repeat until found or boundaries cross
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(arr: List[int], target: int,
                              left: int = 0, right: int = None) -> int:
    """Recursive binary search."""
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def binary_search_traced(arr: List[int], target: int) -> dict:
    """Binary search with step trace for visualization."""
    steps = []
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        steps.append({
            "left": left, "right": right, "mid": mid,
            "value": arr[mid], "target": target,
            "status": "found" if arr[mid] == target else
                      "go_right" if arr[mid] < target else "go_left"
        })

        if arr[mid] == target:
            return {"result": mid, "steps": steps}
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return {"result": -1, "steps": steps}
