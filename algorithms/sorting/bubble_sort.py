"""
Bubble Sort
============

Repeatedly steps through the list, compares adjacent elements,
and swaps them if they are in the wrong order.

The "bubble" name comes from smaller elements "bubbling" to the top.

Time Complexity:
    Best:    O(n)   — already sorted (with optimization)
    Average: O(n²)
    Worst:   O(n²)

Space Complexity: O(1) — in-place

Real-world: Rarely used in practice due to O(n²), but great for teaching.
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using bubble sort.

    Steps:
        1. Compare each pair of adjacent elements
        2. Swap them if they are in the wrong order
        3. Repeat until no more swaps are needed
        4. After each pass, the largest unsorted element
           is in its correct position
    """
    n = len(arr)

    for i in range(n):
        swapped = False

        # Step 1-2: Compare and swap adjacent elements
        # After each pass i, the last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Step 3: Optimization — if no swaps, array is sorted
        if not swapped:
            break

    return arr


def bubble_sort_traced(arr: List[int]) -> dict:
    """
    Bubble sort with step-by-step trace for visualization.

    Returns:
        {
            "sorted": [...],
            "steps": [
                {"type": "compare", "indices": [i, j], "array": [...]},
                {"type": "swap", "indices": [i, j], "array": [...]},
                ...
            ]
        }
    """
    arr = list(arr)  # Copy
    steps = [{"type": "initial", "indices": [], "array": list(arr)}]
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            steps.append({"type": "compare", "indices": [j, j + 1], "array": list(arr)})

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                steps.append({"type": "swap", "indices": [j, j + 1], "array": list(arr)})

        if not swapped:
            break

    steps.append({"type": "done", "indices": [], "array": list(arr)})
    return {"sorted": arr, "steps": steps}
