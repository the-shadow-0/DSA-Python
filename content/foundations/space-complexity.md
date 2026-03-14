# Memory Internals: Beyond O(n)

Space complexity analysis must consider how memory is allocated and deallocated by the Python runtime.

## The Python Heap vs the Stack
- **Stack**: Stores primitive variables and function call frames. Fast, small, automatically managed.
- **Heap**: Stores all objects (`list`, `dict`, `custom_class`). Sized and managed by the Garbage Collector.

## Reference Counting and Garbage Collection
Python uses reference counting to track how many pointers refer to an object.
1. When ref count hits 0, memory is immediately freed.
2. For "Cyclic References" (A points to B, B points to A), Python has a cyclic generational garbage collector.

## Memory Profiling Checklist
- **Input Space**: Does your function store the input? (Usually ignored in auxiliary analysis).
- **Stack Space**: How deep does the recursion go?
- **Heap Space**: Are you creating new collections or modifying in-place (in-situ)?

## Optimization: In-place Algorithms
An in-place algorithm uses `O(1)` extra space (ignoring recursion stack).
- **Example**: QuickSort's partition.
- **Anti-example**: MergeSort's merge requires a temporary array of size `n` (`O(n)` space).

## Advanced: Bit Complexity
Sometimes, if the numbers grow very large, we must consider the number of bits required to store them.
- In `O(n)` logic where `n` is a 1000-digit number, math operations are no longer `O(1)`.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Space Complexity?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Space Complexity compare to other structures in its class?**
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


## 🚀 Multi-Implementation Mastery: Space Scaling

### Way 3: O(n) Recursive Depth Space
```python
def depth(n): if n == 0: return; depth(n-1)
# Consumes O(n) stack space
```

### Way 4: O(1) Iterative space constant
```python
for i in range(n): sum += i # Space is always just 'sum'
```
