"""
Linked List
============

A linked list stores elements in nodes, where each node points to the next.
Unlike arrays, elements are not stored contiguously in memory.

Real-world usage:
    - Browser history (back/forward navigation)
    - Music playlists (next/previous song)
    - Undo/redo functionality

Time Complexities:
    Access:    O(n)  — must traverse from head
    Search:    O(n)
    Insert:    O(1)  — at head or given node
    Delete:    O(1)  — given node reference
"""

from typing import Any, Optional, List


class ListNode:
    """A single node in a linked list."""

    def __init__(self, value: Any, next_node: Optional['ListNode'] = None):
        self.value = value
        self.next = next_node

    def __repr__(self):
        return f"ListNode({self.value})"


class LinkedList:
    """
    Singly Linked List implementation.

    Supports: insert_head, insert_tail, delete, search, reverse, to_list.
    """

    def __init__(self):
        self.head: Optional[ListNode] = None
        self.size: int = 0

    def insert_head(self, value: Any) -> None:
        """
        Insert a new node at the head of the list.

        Time Complexity:  O(1)
        Space Complexity: O(1)

        Steps:
            1. Create a new node
            2. Point new node's next to current head
            3. Update head to new node
        """
        # Step 1: Create new node pointing to current head
        new_node = ListNode(value, self.head)
        # Step 2: Update head
        self.head = new_node
        self.size += 1

    def insert_tail(self, value: Any) -> None:
        """
        Insert a new node at the tail of the list.

        Time Complexity:  O(n) — must traverse to end
        Space Complexity: O(1)
        """
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
        else:
            # Traverse to the last node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self.size += 1

    def delete(self, value: Any) -> bool:
        """
        Delete the first node with the given value.

        Time Complexity:  O(n)
        Space Complexity: O(1)

        Steps:
            1. Handle edge case — deleting head
            2. Traverse to find the node before the target
            3. Update pointers to skip the target node
        """
        if not self.head:
            return False

        # Step 1: If head is the target, update head
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return True

        # Step 2: Find the node before the target
        current = self.head
        while current.next:
            if current.next.value == value:
                # Step 3: Skip over the target node
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        return False  # Value not found

    def search(self, value: Any) -> Optional[int]:
        """
        Search for a value, return its index or None.

        Time Complexity:  O(n)
        Space Complexity: O(1)
        """
        current = self.head
        index = 0

        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1

        return None

    def reverse(self) -> None:
        """
        Reverse the linked list in-place.

        Time Complexity:  O(n)
        Space Complexity: O(1)

        Steps:
            1. Initialize three pointers: prev, current, next
            2. For each node, reverse its pointer direction
            3. Update head to the last node
        """
        prev = None
        current = self.head

        while current:
            # Save next node before we change the pointer
            next_node = current.next
            # Reverse the pointer
            current.next = prev
            # Move prev and current forward
            prev = current
            current = next_node

        # Update head to the new front (previously the last node)
        self.head = prev

    def to_list(self) -> List[Any]:
        """Convert linked list to Python list for easy viewing."""
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        return self.size

    def __repr__(self):
        values = self.to_list()
        return " -> ".join(str(v) for v in values) + " -> None"
