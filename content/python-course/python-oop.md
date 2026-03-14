# Professional OOP: Beyond Classes

Python's Object-Oriented Programming is incredibly flexible, supporting multiple inheritance and metaprogramming.

## Multiple Inheritance and MRO
Python uses the C3 Linearization algorithm to determine the **Method Resolution Order (MRO)**.
```python
class A:
    def greet(self): print("A")
class B(A):
    def greet(self): print("B")
class C(A):
    def greet(self): print("C")
class D(B, C):
    pass

d = D()
d.greet() # Output: B
print(D.mro()) # [D, B, C, A, object]
```

## Property Decorators
Use `@property` for getter/setter logic instead of manual methods.
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0: raise ValueError
        self._radius = value
```

## Abstract Base Classes (ABCs)
Enforce that subclasses implement specific methods.
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

## Class vs Static Methods
- `@classmethod`: Receives the class (`cls`) as the first argument. Useful for factory methods.
- `@staticmethod`: No automatic first argument. Just a normal function grouped inside a class.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Python Oop?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Python Oop compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: OOP Patterns: OOP Patterns

### Way 1: Standard Class with __init__
```python
class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
```

### Way 2: Modern DataClass (Python 3.7+)
```python
from dataclasses import dataclass
@dataclass
class User:
    id: int
    name: str
```


### Way 3: Abstract Base Classes (Interfacing)
```python
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
```

### Way 4: Structural Typing (Protocols)
```python
from typing import Protocol
class Drawable(Protocol):
    def draw(self) -> None: ...
```

## 🌍 Real-World Use Case
**Scenario**: Modeling Database Entities and JSON responses.
*Why it matters*: Real-world systems prioritize either maintenance simplicity or raw execution speed depending on scale.

