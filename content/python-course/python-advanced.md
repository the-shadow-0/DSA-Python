# Master Tier Python: Metaprogramming & Introspection

## Decorators with Arguments
To create a decorator that takes arguments, you need an extra level of nesting.
```python
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi(): print("Hi!")
```

## Iterators and Iterables
- **Iterable**: An object that can return its members one at a time.
- **Iterator**: The object used to perform the iteration (maintains state).
Implementing `__iter__` and `__next__` makes your class an iterator.

## Memory Efficient Generators
Generators use "Lazy Evaluation". They don't store the whole result in memory; they calculate the next value on the fly.
```python
def huge_data_stream():
    for i in range(10**12): # Trillions of items
        yield i
```

## Context Managers (The `__enter__` and `__exit__` magic)
You can build your own `with` statement support.
```python
class MyTimer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Elapsed: {time.time() - self.start}")
```

## Map, Filter, and Reduce
Functional programming tools.
```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x*x, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
```

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Python Advanced?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Python Advanced compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Advanced Patterns: Generators & Iterators

### Way 1: Standard List Creation
```python
def get_nums(n):
    return [x for x in range(n)]
```

### Way 2: Yield-based Generator (Memory Efficient)
```python
def get_nums(n):
    for x in range(n):
        yield x
```


### Way 3: Context Managers (Class-based)
```python
class DBConn:
    def __enter__(self): return self
    def __exit__(self, *args): pass
```

### Way 4: Contextlib @contextmanager (Functional)
```python
from contextlib import contextmanager
@contextmanager
def temp_file(): yield; print('Cleaned up!')
```

## 🌍 Real-World Use Case
**Scenario**: Parsing multi-gigabyte log files without crashing memory.
*Why it matters*: Real-world systems prioritize either maintenance simplicity or raw execution speed depending on scale.

