# Graph Algorithms: Routing and Flow

Graph traversal is the backbone of social networks, GPS, and internet routing.

## BFS vs DFS: The Internal Difference
- **BFS (Queue)**: Explores "horizontally". Guarantees the shortest path in unweighted graphs because it finds the path with the minimum number of edges.
- **DFS (Stack/Recursion)**: Explores "vertically". Better for finding bridges, cycles, or searching deep trees.

## Dijkstra: The Greedy Pathfinding
1. Set start distance to 0, all others to infinity.
2. Store unvisited nodes in a **Priority Queue (Min-Heap)**.
3. Continuously pick the node with the smallest distance.
4. For each neighbor, check if `dist[current] + edge_weight < dist[neighbor]`.
**Complexity**: `O((V + E) log V)` using a Binary Heap.

## Topological Sort (DAGs Only)
An ordering of tasks where dependencies are respected.
- **Requirement**: The graph must be a **Directed Acyclic Graph (DAG)**. No cycles!
- **Kahn's Algorithm**: Use a queue to track nodes with `in-degree == 0`.

## Minimum Spanning Tree (MST)
Connecting all nodes with the absolute minimum total weight.
- **Kruskal's**: Greedy. Sort edges by weight and add them if they don't form a cycle (use **Union-Find**).
- **Prim's**: Greedy. Build the tree node by node from a starting point (use **Priority Queue**).

## Real-world: PageRank
Google's original algorithm is essentially a variation of graph analysis where "importance" flows through edges (links).

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Graph Algorithms?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Graph Algorithms compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Graph Search: Graph Search

### Way 1: Dijkstra (Matrix-based)
```python
for i in range(n): u = min_dist(dist, visited); visited[u] = True
```

### Way 2: Dijkstra (Priority Queue)
```python
heapq.heappush(pq, (0, start))
```


### Way 3: Bellman-Ford (supports negative weights)
```python
for _ in range(n-1): 
    for u, v, w in edges: 
        dist[v] = min(dist[v], dist[u] + w)
```

### Way 4: A* Search (Heuristic-based)
```python
heapq.heappush(pq, (f_score, start))
# f = g + h (distance + estimate)
```

## 🌍 Real-World Use Case
**Scenario**: Google Maps route finding and GPS navigation.
*Why it matters*: Practical engineering requires a deep understanding of these trade-offs to build resilient systems.

