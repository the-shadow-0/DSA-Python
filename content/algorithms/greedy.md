# Greedy Algorithms: Making the Best Local Choice

A greedy algorithm builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit (**the "greedy" choice**).

## The Greedy Principle
Make the locally optimal choice in the hope that it will lead to a globally optimal solution.

## When Does Greedy Work?
A greedy algorithm only works if the problem has:
1. **Greedy Choice Property**: A global optimum can be reached by making local optimums.
2. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to sub-problems.

## Famous Examples

### 1. Coin Change (Limited Cases)
- Goal: Minimize number of coins.
- Greedy Choice: Take the largest coin possible first.
- Note: This doesn't work for all coin sets! (e.g., coins [1, 3, 4] for 6 cents).

### 2. Huffman Coding
- Goal: Lossless data compression.
- Greedy Choice: Merge the two nodes with the lowest frequency.

### 3. Dijkstra's Algorithm
- Goal: Shortest path in a graph.
- Greedy Choice: Always visit the closest unvisited node.

## Greedy vs Dynamic Programming
- **Greedy**: Fast, makes one choice and never goes back.
- **DP**: Brute-force but remembers, checks all possibilities effectively.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Greedy?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Greedy compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Greedy Strategies: Greedy Strategies

### Way 1: Sorting-based Greedy (Activity Selection)
```python
activities.sort(key=lambda x: x.end); # pick first that starts after last ends
```

### Way 2: Priority Queue-based Greedy (Huffman Coding)
```python
heapq.heappush(heap, node); # constant retrieval of minimum
```


### Way 3: Fractional Knapsack (Value/Weight ratio)
```python
items.sort(key=lambda x: x.v/x.w, reverse=True)
# Greedy choice based on density
```

### Way 4: Kruskal's MST (Sorting edges)
```python
edges.sort(); # Use Union-Find to skip cycles
```

## 🌍 Real-World Use Case
**Scenario**: Bandwidth allocation and data compression algorithms.
*Why it matters*: Practical engineering requires a deep understanding of these trade-offs to build resilient systems.

