# Variables and Data Types: The Deep Dive

In Python, variables are "names" that refer to objects in memory. Understanding how Python handles memory and types is crucial for writing efficient code.

## Internal Memory Model
In Python, everything is an **object**. Even a simple integer like `x = 42` is an object with overhead (value, type, reference count).
- **Immutable Types**: `int`, `float`, `str`, `tuple`, `bool`. Once created, their value cannot change.
- **Mutable Types**: `list`, `dict`, `set`. You can modify them in-place.

## Numeric Types & Precision
- **integers**: Arbitrary precision! Python can handle numbers as large as your RAM allows.
- **floats**: Double-precision (64-bit), following the IEEE 754 standard. Be careful with precision errors (e.g., `0.1 + 0.2 != 0.3`).

## Strings: Unicode and Beyond
Python 3 strings are Unicode. 
```python
s = "Hello"
# String Interning: Python reuses some strings to save memory
a = "hello"
b = "hello"
print(a is b) # True (usually for short, constant strings)
```

## Collection Deep-Dive

### Lists (Dynamic Arrays)
- Over-allocation: Python allocates extra space to avoid frequent resizing.
- Time Complexity: Append is `O(1)` amortized, but `insert(0, val)` is `O(n)`.

### Dictionaries (Hash Maps)
- Since Python 3.7, dictionaries maintain insertion order.
- Average lookup is `O(1)`.

### Sets
- Use them for membership testing. `val in set` is `O(1)` vs `O(n)` for lists.

## Type Hinting (PEP 484)
Modern Python uses type hints to improve readability and catch bugs.
```python
def process_data(data: list[int]) -> int:
    return sum(data)
```

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Python Basics?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Python Basics compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Variables & Types: Variables & Types

### Way 1: Standard Dynamic Typing
```python
user_id = 99
user_name = 'Alice'
score = 100.5
```

### Way 2: Strongly Typed Hinting (PEP 484)
```python
user_id: int = 99
user_name: str = 'Alice'
score: float = 100.5
```


### Way 3: Low-level Memory Profiling (using `sys.getsizeof`)
```python
import sys
x = 42
print(f'Value: {x}, Size: {sys.getsizeof(x)} bytes')
# Note: Even small ints have overhead in Python
```

### Way 4: Static Analysis with Final (Python 3.8+)
```python
from typing import Final
MAX_USERS: Final = 100
# MAX_USERS = 101 # MyPy will flag this as an error
```

## 🌍 Real-World Use Case
**Scenario**: Financial systems where type clarity prevents rounding errors and logic bugs.
*Why it matters*: Real-world systems prioritize either maintenance simplicity or raw execution speed depending on scale.

