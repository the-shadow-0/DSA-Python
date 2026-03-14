# Advanced Control Flow

Beyond simple `if` and `for`, Python offers powerful patterns for managing logic.

## The `Walrus` Operator (`:=`)
Introduced in Python 3.8, it allows you to assign a value to a variable within an expression.
```python
if (n := len(my_list)) > 10:
    print(f"List is too long: {n} elements")
```

## For-Else and While-Else
The `else` block in a loop executes **only if the loop completes successfully** (without hitting a `break`).
```python
for x in [1, 2, 3]:
    if x == 4: break
else:
    print("4 was not found!") # This runs
```

## Truthiness in Python
Objects have a "truth" value.
- **Falsy**: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`.
- **Truthy**: Practically everything else.

## Structural Pattern Matching (Python 3.10+)
Similar to "switch" in other languages but far more powerful.
```python
def handle_command(cmd):
    match cmd.split():
        case ["quit"]:
            print("Quitting...")
        case ["load", filename]:
            print(f"Loading {filename}")
        case ["move", x, y] if int(y) > 0:
            print(f"Moving to {x}, {y}")
        case _:
            print("Unknown command")
```

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Python Control Flow?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Python Control Flow compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Loops & Logic: Loops & Logic

### Way 1: Procedural For-Loop
```python
evens = []
for i in range(20):
    if i % 2 == 0: evens.append(i)
```

### Way 2: Functional List Comprehension
```python
evens = [i for i in range(20) if i % 2 == 0]
```


### Way 3: Itertools for Complex Loops
```python
import itertools
for item in itertools.cycle(['A', 'B', 'C']): # Perfect for round-robin
    print(item)
    break
```

### Way 4: Switch-Case Pattern (Match/Case - Python 3.10+)
```python
def handle_status(code):
    match code:
        case 200: return 'OK'
        case 404: return 'Not Found'
        case _: return 'Error'
```

## 🌍 Real-World Use Case
**Scenario**: Processing stream data in real-time dashboards.
*Why it matters*: Real-world systems prioritize either maintenance simplicity or raw execution speed depending on scale.

