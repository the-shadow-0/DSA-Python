# Deep-Dive: Calculating Time Complexity

Calculating complexity in the real world requires looking past simple loops.

## The Call Stack and Recursion
A recursive function's time complexity is usually `Number of Calls * Work per Call`.

### The Fibonacci Disaster
```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```
- Each call branches into 2 more.
- Depth is `n`.
- Total calls: `2⁰ + 2¹ + 2² + ... + 2ⁿ⁻¹ = 2ⁿ - 1`.
- Complexity: `O(2ⁿ)`.

## Mastery Tip: Master Theorem
Used to solve recurrences of the form `T(n) = aT(n/b) + f(n)`.
- **Merge Sort**: `T(n) = 2T(n/2) + O(n)` -> `O(n log n)`.
- **Binary Search**: `T(n) = T(n/2) + O(1)` -> `O(log n)`.

## Sorting Complexity: The Lower Bound
Why is `n log n` the best we can do for comparison-based sorting?
- Any comparison-based sort can be represented as a binary decision tree.
- A tree of height `h` has `2ˡ` leaves.
- To sort `n` items, we need at least `n!` leaves (all permutations).
- `2ˡ ≥ n!`
- `h ≥ log(n!)`
- By Stirling's approximation, `log(n!) ≈ n log n`.

## Practical Bottlenecks
- **I/O Bound**: Waiting for disk or network.
- **CPU Bound**: Pure computation.
- **Memory Bound**: Waiting for RAM (Cache misses).

Understanding Big O helps you identify when your code is CPU bound vs architecture bound.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Time Complexity?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Time Complexity compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Time Metrics: Time Complexity

### Way 1: Measure using `time.perf_counter()`
```python
start = time.perf_counter(); my_func(); print(time.perf_counter() - start)
```

### Way 2: Analyze using `timeit.timeit()`
```python
import timeit; timeit.timeit('my_func()', globals=globals(), number=1000)
```


### Way 3: O(sqrt(n)) Primality Test
```python
for i in range(2, int(n**0.5)+1): if n % i == 0: return False
```

### Way 4: O(log log n) Sieve of Eratosthenes
```python
def sieve(n):
    # Optimized primes generator
```

## 🌍 Real-World Use Case
**Scenario**: Profiling latency-critical service level objectives (SLOs).
*Why it matters*: Choosing the right implementation balances cognitive load with technical performance.

