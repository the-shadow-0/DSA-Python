# Linked Lists: The Pointer Chain Mastery

Linked lists are the ultimate test of "pointer manipulation" skills.

## Singly vs Doubly Linked: Memory Overhead
- **Singly**: 1 Pointer per node (Next). `O(n)` to delete the last node.
- **Doubly**: 2 Pointers per node (Prev + Next). `O(1)` to delete a node if you already have a reference to it.

## The "Dummy Head" Pattern (Crucial Technique)
When building or modifying a linked list, creating a dummy starting node simplifies logic by removing the `if head is None` check.

```python
def merge_lists(l1, l2):
    dummy = Node(0)
    current = dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next, l1 = l1, l1.next
        else:
            current.next, l2 = l2, l2.next
        current = current.next
    current.next = l1 or l2
    return dummy.next
```

## Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
To detect a loop in `O(n)` space and `O(1)` time:
1. Two pointers, `slow` (moves 1 step) and `fast` (moves 2 steps).
2. If they ever meet, there is a cycle.

## Real-world Usage: Linux Kernel
The Linux kernel uses doubly linked lists for almost everything (task management, drivers, etc.).

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Linked Lists?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Linked Lists compare to other structures in its class?**
   - *Answer*: Contrast with related topics (e.g., Arrays vs Linked Lists).

### Thought Process
- **Understand the Constraints**: Ask about the size of input and memory limits.
- **Base Cases**: Always define the simplest form of the problem first.
- **Optimal Strategy**: Mention why the chosen approach is the most efficient.

## 📋 Cheat Sheet

| Metric | Complexity |
|---|---|
| Average Case | O(1) - O(n log n) |
| Worst Case | See specific analysis above |
| Space Used | Auxiliary space details |

## ⚠️ Common Pitfalls

- **Off-by-one Errors**: The most common mistake in indexing.
- **Memory Leaks**: Forgetting to clean up pointers in low-level implementations.
- **Infinite Recursion**: Missing or incorrect base cases.

## 🚀 Multi-Implementation Mastery: Linked Lists: Linked Lists

### Way 1: Iterative Reversal
```python
prev = None
curr = head
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
```

### Way 2: Recursive Reversal
```python
def reverse(node, prev=None):
    if not node: return prev
    nxt = node.next
    node.next = prev
    return reverse(nxt, node)
```


### Way 3: Doubly Linked List (Prev + Next)
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None
```

### Way 4: Circular Linked List (Tail.next = Head)
```python
# Tail node points back to head for infinite cycling
head.next = tail; tail.next = head
```

## 🌍 Real-World Use Case
**Scenario**: Low-level memory management and LRU cache implementations.
*Why it matters*: Real-world systems prioritize either maintenance simplicity or raw execution speed depending on scale.

