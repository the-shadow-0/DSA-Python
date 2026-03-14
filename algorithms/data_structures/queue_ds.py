"""
Queue
======

A queue is a First-In-First-Out (FIFO) data structure.
Think of a line at a grocery store — first person in line is served first.

Real-world usage:
    - Print job scheduling
    - Web server request handling
    - BFS graph traversal
    - Message queues (RabbitMQ, Kafka)

Time Complexities:
    Enqueue: O(1)
    Dequeue: O(1)
    Peek:    O(1)
"""

from typing import Any, List
from collections import deque


class Queue:
    """
    Queue implementation using collections.deque for O(1) operations.

    Operations: enqueue, dequeue, peek, is_empty, size.
    """

    def __init__(self):
        self._items: deque = deque()

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the back of the queue.

        Time Complexity: O(1)
        """
        self._items.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the front item.

        Time Complexity: O(1)

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft()

    def peek(self) -> Any:
        """
        Return the front item without removing it.

        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty. O(1)."""
        return len(self._items) == 0

    @property
    def size(self) -> int:
        """Number of items in the queue. O(1)."""
        return len(self._items)

    def __len__(self):
        return self.size

    def __repr__(self):
        return f"Queue(front → {list(self._items)})"


class PriorityQueue:
    """
    Priority Queue using a min-heap.

    Items with lower priority values are dequeued first.

    Real-world usage:
        - Emergency room triage
        - OS process scheduling
        - Dijkstra's algorithm
    """

    def __init__(self):
        self._heap: List = []

    def enqueue(self, item: Any, priority: int) -> None:
        """
        Add an item with a priority value.

        Time Complexity: O(log n)
        """
        import heapq
        heapq.heappush(self._heap, (priority, item))

    def dequeue(self) -> Any:
        """
        Remove and return the highest-priority (lowest value) item.

        Time Complexity: O(log n)
        """
        import heapq
        if not self._heap:
            raise IndexError("Dequeue from empty priority queue")
        _, item = heapq.heappop(self._heap)
        return item

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    @property
    def size(self) -> int:
        return len(self._heap)

    def __repr__(self):
        return f"PriorityQueue({self._heap})"
