# Functions, Scope, and Closures

Functions in Python are **first-class objects**. You can pass them as arguments, return them from other functions, and store them in data structures.

## Scope Resolution: LEGB Rule
Python searches for variables in this specific order:
1. **L**ocal: Inside the current function.
2. **E**nclosing: In the outer function (for nested functions).
3. **G**lobal: In the module top-level.
4. **B**uilt-in: Python's pre-installed names (`len`, `sum`, etc.).

## Closures
A closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
```python
def outer(msg):
    def inner():
        print(msg)
    return inner

hi_func = outer("Hello")
hi_func() # Still remembers "Hello"!
```

## Lambda Functions
Anonymous, one-line functions.
```python
square = lambda x: x * x
print(square(5)) # 25
```

## Function Annotations and Docs
Use docstrings to document your API.
```python
def add(a: int, b: int) -> int:
    """Sum two integers and return the result."""
    return a + b
```

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Python Functions?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Python Functions compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Functions: Functions

### Way 1: Standard Def Declaration
```python
def square(n):
    return n * n
```

### Way 2: Anonymous Lambda Functions
```python
square = lambda n: n * n
```


### Way 3: Higher-Order Functions & Map/Filter
```python
nums = [1, 2, 3]
squared = list(map(lambda x: x*x, nums))
# Efficient functional-style processing
```

### Way 4: Partial Function Application
```python
from functools import partial
def power(base, exp): return base ** exp
square = partial(power, exp=2)
print(square(10)) # 100
```

## 🌍 Real-World Use Case
**Scenario**: Higher-order operations like sorting complex objects in Pandas.
*Why it matters*: Real-world systems prioritize either maintenance simplicity or raw execution speed depending on scale.

