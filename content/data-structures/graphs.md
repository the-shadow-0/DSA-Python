# Graphs: Modeling Connections

A graph is a data structure consisting of a set of vertices (nodes) and a set of edges connecting them. It is used to model networks.

## Types of Graphs
1. **Directed**: Edges have a direction (e.g., Twitter followers).
2. **Undirected**: Edges work both ways (e.g., Facebook friends).
3. **Weighted**: Edges have a cost or distance (e.g., Google Maps distances).
4. **Cyclic/Acyclic**: Does the graph have loops?

## Representations

### 1. Adjacency Matrix
A 2D array where `matrix[i][j] = 1` if an edge exists.
- **Pros**: Fast lookup.
- **Cons**: Wasteful `O(V²)` space for sparse graphs.

### 2. Adjacency List
A dictionary where each node points to a list of its neighbors.
- **Pros**: Efficient `O(V + E)` space.
- **Cons**: Slower lookup.

```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

## Traversal Algorithms

1. **DFS (Depth First Search)**: Go as deep as possible, then backtrack. (Uses a Stack).
2. **BFS (Breadth First Search)**: Explore level by level. (Uses a Queue).

## Real-world Applications
1. **Social Networks**: Users and friendships.
2. **GPS / Maps**: Cities and roads.
3. **Recommendation Engines**: Amazon's "Customers who bought this also bought..."
4. **Internet Routing**: Packets moving between nodes.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Graphs?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Graphs compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Graph Representations: Graph Representations

### Way 1: Adjacency Matrix
```python
matrix = [[0]*n for _ in range(n)]
```

### Way 2: Adjacency List (Dictionary)
```python
adj = collections.defaultdict(list)
```


### Way 3: Transposed Graph (Reverse all edges)
```python
tg = collections.defaultdict(list)
for u in g: for v in g[u]: tg[v].append(u)
```

### Way 4: Edge List representation
```python
edges = [(u, v, weight), ...]
# Efficient for algorithms like Kruskal's
```

## 🌍 Real-World Use Case
**Scenario**: Mapping physical computer networks and wiring layouts.
*Why it matters*: Practical engineering requires a deep understanding of these trade-offs to build resilient systems.

