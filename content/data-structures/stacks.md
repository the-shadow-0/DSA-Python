# Stacks: Last In, First Out (LIFO)

A stack is a linear data structure that follows the principle: the last element added is the first one to be removed.

## Analogy
Think of a stack of plates. You put the newest plate on top, and you take the top plate off first.

## Core Operations

1. **Push**: Add an element to the top. `O(1)`
2. **Pop**: Remove the top element. `O(1)`
3. **Peek**: Look at the top element without removing it. `O(1)`
4. **isEmpty**: Check if the stack is empty. `O(1)`

## Python Implementation
You can use a list as a stack efficiently.

```python
stack = []
stack.append(1) # Push
stack.append(2)
top = stack.pop() # Pop -> returns 2
```

## Real-world Applications

1. **Undo/Redo**: Maintains the history of changes.
2. **Function Calls**: The CPU uses a stack (Call Stack) to handle functions calling functions.
3. **Expression Parsing**: Used in compilers to handle math expressions like `(2 + 3) * 5`.
4. **Backtracking**: Used in maze-solving or chess algorithms to go back to a previous state.

## Stack Overflow
A stack overflow occurs when the call stack exceeds its memory limit, usually due to infinite recursion.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Stacks?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Stacks compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Stacks: Stacks

### Way 1: Using `list.append()`/`list.pop()`
```python
s = []; s.append(1); val = s.pop()
```

### Way 2: Using `collections.deque`
```python
from collections import deque; s = deque(); s.append(1); s.pop()
```


### Way 3: LIFO Cache with `queue.LifoQueue` (Thread-safe)
```python
from queue import LifoQueue
stack = LifoQueue(maxsize=10)
stack.put(1); val = stack.get()
```

### Way 4: Stack with Tracking Max (O(1) getMax)
```python
data = []; max_stack = []
def push(x): 
    data.append(x)
    m = max(x, max_stack[-1] if max_stack else x)
    max_stack.append(m)
```

## 🌍 Real-World Use Case
**Scenario**: Function call stacks and undo history.
*Why it matters*: Choosing the right implementation balances cognitive load with technical performance.

