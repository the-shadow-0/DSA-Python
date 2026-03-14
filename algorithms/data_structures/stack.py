"""
Stack
======

A stack is a Last-In-First-Out (LIFO) data structure.
Think of a stack of plates — you add and remove from the top.

Real-world usage:
    - Undo system in text editors (Ctrl+Z)
    - Browser back button
    - Function call stack in programming languages
    - Expression evaluation (parentheses matching)

Time Complexities:
    Push:  O(1)
    Pop:   O(1)
    Peek:  O(1)
"""

from typing import Any, Optional, List


class Stack:
    """
    Stack implementation using a Python list.

    Operations: push, pop, peek, is_empty, size.
    """

    def __init__(self):
        self._items: List[Any] = []

    def push(self, item: Any) -> None:
        """
        Add an item to the top of the stack.

        Time Complexity:  O(1) amortized
        Space Complexity: O(1)
        """
        self._items.append(item)

    def pop(self) -> Any:
        """
        Remove and return the top item.

        Time Complexity:  O(1)
        Space Complexity: O(1)

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        """
        Return the top item without removing it.

        Time Complexity:  O(1)
        """
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty. O(1)."""
        return len(self._items) == 0

    @property
    def size(self) -> int:
        """Number of items in the stack. O(1)."""
        return len(self._items)

    def __len__(self):
        return self.size

    def __repr__(self):
        return f"Stack(top → {list(reversed(self._items))})"


# ──────────────────────────────────────────────
# Classic Stack Problem: Valid Parentheses
# ──────────────────────────────────────────────
def is_valid_parentheses(s: str) -> bool:
    """
    Check if a string of brackets is properly nested.

    Time Complexity:  O(n)
    Space Complexity: O(n)

    Steps:
        1. Push every opening bracket onto the stack
        2. For every closing bracket, check if it matches the top
        3. If the stack is empty at the end, brackets are valid

    Example:
        "([]{})" → True
        "([)]"   → False
    """
    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            # Step 1: Push opening brackets
            stack.push(char)
        elif char in ')]}':
            # Step 2: Check if closing bracket matches top
            if stack.is_empty() or stack.pop() != matching[char]:
                return False

    # Step 3: Valid if stack is empty (all brackets matched)
    return stack.is_empty()
