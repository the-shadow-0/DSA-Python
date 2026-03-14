"""
Insertion Sort
===============

Builds the sorted array one element at a time by inserting
each element into its correct position.

Time Complexity:
    Best:    O(n)   — already sorted
    Average: O(n²)
    Worst:   O(n²)

Space Complexity: O(1)

Real-world: Excellent for small or nearly-sorted arrays.
            Used as the base case in Timsort (Python's built-in sort).
"""

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sort using insertion sort.

    Steps:
        1. Start from the second element (index 1)
        2. Compare it with elements to its left
        3. Shift larger elements right
        4. Insert the element in its correct position
    """
    for i in range(1, len(arr)):
        # Step 1: Pick the current element
        key = arr[i]
        j = i - 1

        # Step 2-3: Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Step 4: Insert key in correct position
        arr[j + 1] = key

    return arr


def insertion_sort_traced(arr: List[int]) -> dict:
    """Insertion sort with step trace for visualization."""
    arr = list(arr)
    steps = [{"type": "initial", "indices": [], "array": list(arr)}]

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        steps.append({"type": "select", "indices": [i], "array": list(arr)})

        while j >= 0 and arr[j] > key:
            steps.append({"type": "compare", "indices": [j, j + 1], "array": list(arr)})
            arr[j + 1] = arr[j]
            j -= 1
            steps.append({"type": "shift", "indices": [j + 1, j + 2], "array": list(arr)})

        arr[j + 1] = key
        steps.append({"type": "insert", "indices": [j + 1], "array": list(arr)})

    steps.append({"type": "done", "indices": [], "array": list(arr)})
    return {"sorted": arr, "steps": steps}
