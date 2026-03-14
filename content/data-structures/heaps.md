# Heaps: Arrays as Trees

A binary heap is a **Complete Binary Tree** mapped onto an array. This mapping is why heaps are so memory-efficient.

## The Logical vs Physical View
- **Logical**: A tree where children are ≥ parent.
- **Physical**: `[min, child1, child2, grandchild1, ...]`

## Navigation Math
For node at index `i`:
- `Left = 2i + 1`
- `Right = 2i + 2`
- `Parent = (i - 1) // 2`

## Building a Heap (Heapify)
If you have an array of `n` items, you can build a heap in `O(n)` time, not `O(n log n)`.
- We only need to call `sink_down()` on the first half of the array.
- The work decreases as we move towards the leaves.

## Priority Queues
In Python, `heapq` only provides a **Min-Heap**. To get a **Max-Heap**:
- Negate the values: `heapq.heappush(h, -val)`.
- When popping, negate back: `val = -heapq.heappop(h)`.

## Use Case: K-Largest Elements
To find the 100 largest items in a stream of millions:
1. Maintain a Min-Heap of size 100.
2. For every new item, if it's > `heap[0]`, pop and push the new item.
3. Time: `O(N log K)`. Memory: `O(K)`.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Heaps?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Heaps compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Heaps: Heaps

### Way 1: Max-Heap using `heapq` (Negated)
```python
import heapq; l = []; heapq.heappush(l, -val)
```

### Way 2: Min-Heap using `heapq` (Standard)
```python
import heapq; l = []; heapq.heappush(l, val)
```


### Way 3: Min-Max Heap (supports both Min/Max in O(1))
```python
# Complex structure requiring level-based comparisons
```

### Way 4: Pythonic Heap Merge
```python
import heapq
merged = heapq.merge([1, 3, 5], [2, 4, 6])
# Lazy iterator over multiple sorted inputs
```

## 🌍 Real-World Use Case
**Scenario**: Real-time task priority scoring and median finding.
*Why it matters*: Practical engineering requires a deep understanding of these trade-offs to build resilient systems.

