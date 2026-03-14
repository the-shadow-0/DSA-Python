"""
Selection Sort
===============

Finds the minimum element in the unsorted portion and swaps it
with the first unsorted element.

Time Complexity:  O(n²) always
Space Complexity: O(1)

Real-world: Simple but inefficient; used when memory writes are expensive.
"""

from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    """
    Sort using selection sort.

    Steps:
        1. Find the minimum element in unsorted portion
        2. Swap it with the first unsorted element
        3. Move the boundary between sorted and unsorted portions
        4. Repeat until fully sorted
    """
    n = len(arr)

    for i in range(n):
        # Step 1: Find minimum in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Step 2: Swap minimum with current position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


def selection_sort_traced(arr: List[int]) -> dict:
    """Selection sort with step trace for visualization."""
    arr = list(arr)
    steps = [{"type": "initial", "indices": [], "array": list(arr)}]
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps.append({"type": "compare", "indices": [min_idx, j], "array": list(arr)})
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            steps.append({"type": "swap", "indices": [i, min_idx], "array": list(arr)})

    steps.append({"type": "done", "indices": [], "array": list(arr)})
    return {"sorted": arr, "steps": steps}
