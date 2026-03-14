"""
Segment Tree
=============

A tree data structure for efficient range queries and point updates
on an array.

Supports:
    - Range sum query
    - Range minimum query
    - Point update

Time Complexities:
    Build:       O(n)
    Query:       O(log n)
    Update:      O(log n)

Space Complexity: O(n)

Real-world:
    - Database range queries
    - Computational geometry
    - Competitive programming
"""

from typing import List, Callable


class SegmentTree:
    """
    Segment Tree for range queries.

    Default operation is sum, but can be configured for min, max, etc.
    """

    def __init__(self, data: List[int],
                 operation: Callable = lambda a, b: a + b,
                 identity: int = 0):
        """
        Build a segment tree from data.

        Args:
            data: Input array.
            operation: Binary operation (sum, min, max, etc.).
            identity: Identity element (0 for sum, inf for min, -inf for max).
        """
        self.n = len(data)
        self.operation = operation
        self.identity = identity
        self.tree = [identity] * (4 * self.n)
        if self.n > 0:
            self._build(data, 1, 0, self.n - 1)

    def _build(self, data: List[int], node: int, start: int, end: int):
        """Build the segment tree recursively."""
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self._build(data, 2 * node, start, mid)
            self._build(data, 2 * node + 1, mid + 1, end)
            self.tree[node] = self.operation(self.tree[2 * node],
                                              self.tree[2 * node + 1])

    def query(self, left: int, right: int) -> int:
        """
        Query the range [left, right] (inclusive).

        Time Complexity: O(log n)
        """
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node: int, start: int, end: int,
               left: int, right: int) -> int:
        if right < start or end < left:
            return self.identity  # Out of range
        if left <= start and end <= right:
            return self.tree[node]  # Fully within range

        mid = (start + end) // 2
        left_result = self._query(2 * node, start, mid, left, right)
        right_result = self._query(2 * node + 1, mid + 1, end, left, right)
        return self.operation(left_result, right_result)

    def update(self, index: int, value: int) -> None:
        """
        Update the value at index.

        Time Complexity: O(log n)
        """
        self._update(1, 0, self.n - 1, index, value)

    def _update(self, node: int, start: int, end: int,
                index: int, value: int) -> None:
        if start == end:
            self.tree[node] = value
        else:
            mid = (start + end) // 2
            if index <= mid:
                self._update(2 * node, start, mid, index, value)
            else:
                self._update(2 * node + 1, mid + 1, end, index, value)
            self.tree[node] = self.operation(self.tree[2 * node],
                                              self.tree[2 * node + 1])
