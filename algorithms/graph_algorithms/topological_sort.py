"""
Topological Sort
=================

Linearly orders vertices in a directed acyclic graph (DAG) such that
for every directed edge (u, v), u comes before v.

Time Complexity:  O(V + E)
Space Complexity: O(V)

Real-world:
    - Task scheduling (prerequisites)
    - Build systems (compile order)
    - Course prerequisite ordering
    - Package dependency resolution
"""

from typing import Any, Dict, List, Set
from collections import deque


def topological_sort_dfs(graph: Dict[Any, List[Any]]) -> List[Any]:
    """
    Topological sort using DFS.

    Steps:
        1. For each unvisited vertex, run DFS
        2. After visiting all descendants, push vertex to stack
        3. The reverse of the stack is the topological order
    """
    visited: Set[Any] = set()
    stack: List[Any] = []

    def _dfs(vertex: Any):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                _dfs(neighbor)
        # Push after all descendants are processed
        stack.append(vertex)

    # Visit all vertices (handles disconnected components)
    for vertex in graph:
        if vertex not in visited:
            _dfs(vertex)

    # Reverse gives topological order
    return list(reversed(stack))


def topological_sort_kahn(graph: Dict[Any, List[Any]]) -> List[Any]:
    """
    Topological sort using Kahn's algorithm (BFS-based).

    Steps:
        1. Calculate in-degree for all vertices
        2. Add all zero in-degree vertices to queue
        3. While queue is not empty:
           a. Dequeue a vertex, add to result
           b. Reduce in-degree of all its neighbors by 1
           c. If a neighbor's in-degree becomes 0, add to queue
        4. If result contains all vertices → valid ordering
           If not → graph has a cycle (not a DAG)
    """
    # Step 1: Calculate in-degrees
    in_degree: Dict[Any, int] = {v: 0 for v in graph}
    for vertex in graph:
        for neighbor in graph.get(vertex, []):
            in_degree[neighbor] = in_degree.get(neighbor, 0) + 1

    # Step 2: Collect zero in-degree vertices
    queue: deque = deque([v for v in in_degree if in_degree[v] == 0])
    result: List[Any] = []

    while queue:
        # Step 3a: Process vertex
        vertex = queue.popleft()
        result.append(vertex)

        # Step 3b-c: Update neighbors
        for neighbor in graph.get(vertex, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check for cycles
    if len(result) != len(in_degree):
        raise ValueError("Graph has a cycle — topological sort not possible")

    return result
