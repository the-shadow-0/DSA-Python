"""
Heap (Min-Heap & Max-Heap)
===========================

A heap is a complete binary tree satisfying the heap property:
    - Min-Heap: parent ≤ children (root is the minimum)
    - Max-Heap: parent ≥ children (root is the maximum)

Heaps are stored as arrays — no need for node pointers!
    Parent of i:      (i - 1) // 2
    Left child of i:  2 * i + 1
    Right child of i: 2 * i + 2

Real-world usage:
    - Priority queues (task scheduling)
    - Heap sort
    - Dijkstra's shortest path algorithm
    - Finding top-K elements

Time Complexities:
    Insert:     O(log n)
    Extract:    O(log n)
    Peek:       O(1)
    Build heap: O(n)
"""

from typing import List, Any, Optional


class MinHeap:
    """
    Min-Heap implementation using an array.

    The smallest element is always at the root (index 0).
    """

    def __init__(self):
        self.heap: List[Any] = []

    def insert(self, value: Any) -> None:
        """
        Insert a value into the heap.

        Time Complexity:  O(log n)
        Space Complexity: O(1)

        Steps:
            1. Add the new element at the end (maintain complete tree)
            2. "Bubble up" — swap with parent while smaller than parent
        """
        # Step 1: Add to the end
        self.heap.append(value)

        # Step 2: Bubble up to restore heap property
        self._bubble_up(len(self.heap) - 1)

    def extract_min(self) -> Any:
        """
        Remove and return the minimum element (root).

        Time Complexity:  O(log n)

        Steps:
            1. Save the root (min element)
            2. Move the last element to root
            3. "Bubble down" — swap with smaller child while larger
        """
        if not self.heap:
            raise IndexError("Extract from empty heap")

        # Step 1: Save min
        min_val = self.heap[0]

        # Step 2: Move last element to root
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            # Step 3: Bubble down
            self._bubble_down(0)

        return min_val

    def peek(self) -> Any:
        """Return the minimum element without removing it. O(1)."""
        if not self.heap:
            raise IndexError("Peek from empty heap")
        return self.heap[0]

    def _bubble_up(self, index: int) -> None:
        """Move element up until heap property is restored."""
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                # Swap with parent
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _bubble_down(self, index: int) -> None:
        """Move element down until heap property is restored."""
        size = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            # Check if left child is smaller
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            # Check if right child is smaller
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                # Swap and continue
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    @property
    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def __repr__(self):
        return f"MinHeap({self.heap})"


def heapify(arr: List[int]) -> List[int]:
    """
    Build a min-heap from an unsorted array in-place.

    Time Complexity:  O(n) — not O(n log n)!
    Space Complexity: O(1)

    The trick: start from the last non-leaf node and bubble down each one.
    """
    n = len(arr)

    # Start from last parent node (n//2 - 1) and go backwards
    for i in range(n // 2 - 1, -1, -1):
        _heapify_down(arr, n, i)

    return arr


def _heapify_down(arr: List[int], size: int, index: int) -> None:
    """Helper for heapify — bubble down at given index."""
    smallest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and arr[left] < arr[smallest]:
        smallest = left
    if right < size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        _heapify_down(arr, size, smallest)
