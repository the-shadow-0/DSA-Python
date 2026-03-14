"""
Heap Sort
==========

Uses a max-heap to sort an array in ascending order.

Steps:
    1. Build a max-heap from the array
    2. Repeatedly extract the maximum (root) and place it at the end
    3. Reduce heap size and heapify the root

Time Complexity:  O(n log n) always
Space Complexity: O(1) — in-place

Real-world: Guaranteed O(n log n) worst case, no extra memory.
"""

from typing import List


def heap_sort(arr: List[int]) -> List[int]:
    """Sort using heap sort."""
    n = len(arr)

    # Step 1: Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        _max_heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]

        # Step 3: Heapify the reduced heap
        _max_heapify(arr, i, 0)

    return arr


def _max_heapify(arr: List[int], size: int, root: int) -> None:
    """Ensure the subtree rooted at 'root' satisfies max-heap property."""
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        _max_heapify(arr, size, largest)
