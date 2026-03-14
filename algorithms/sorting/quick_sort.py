"""
Quick Sort
===========

A divide-and-conquer algorithm that picks a "pivot" element,
partitions the array around it, then recursively sorts the partitions.

Time Complexity:
    Best:    O(n log n)
    Average: O(n log n)
    Worst:   O(n²) — when pivot is always the smallest/largest

Space Complexity: O(log n) — recursion stack

Real-world: One of the fastest practical sorting algorithms.
            Used in many language standard libraries.
"""

from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    """
    Sort using quick sort (in-place).

    Steps:
        1. Pick a pivot (last element)
        2. Partition: put everything smaller to the left, larger to the right
        3. Recursively sort left and right partitions
    """
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_helper(arr: List[int], low: int, high: int) -> None:
    if low < high:
        # Step 2: Partition and get pivot index
        pivot_index = _partition(arr, low, high)

        # Step 3: Recursively sort left and right
        _quick_sort_helper(arr, low, pivot_index - 1)
        _quick_sort_helper(arr, pivot_index + 1, high)


def _partition(arr: List[int], low: int, high: int) -> int:
    """
    Lomuto partition scheme.

    Pick the last element as the pivot.
    Rearrange so that all elements < pivot come before it,
    and all elements > pivot come after it.
    """
    pivot = arr[high]
    i = low - 1  # Index of the last element in the "less than" partition

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_traced(arr: List[int]) -> dict:
    """Quick sort with step trace for visualization."""
    arr = list(arr)
    steps = [{"type": "initial", "indices": [], "array": list(arr)}]

    def _sort(low, high):
        if low < high:
            pivot = arr[high]
            steps.append({"type": "pivot", "indices": [high], "array": list(arr)})

            i = low - 1
            for j in range(low, high):
                steps.append({"type": "compare", "indices": [j, high], "array": list(arr)})
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    if i != j:
                        steps.append({"type": "swap", "indices": [i, j], "array": list(arr)})

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            steps.append({"type": "pivot_placed", "indices": [i + 1], "array": list(arr)})

            _sort(low, i)
            _sort(i + 2, high)

    _sort(0, len(arr) - 1)
    steps.append({"type": "done", "indices": [], "array": list(arr)})
    return {"sorted": arr, "steps": steps}
