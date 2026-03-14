"""
Depth-First Search (DFS)
=========================

Explores a graph by going as deep as possible along each branch
before backtracking.

Uses a STACK (or recursion) to track which nodes to visit.

Time Complexity:  O(V + E)
Space Complexity: O(V)

Real-world:
    - Cycle detection
    - Topological sorting
    - Maze solving
    - Detecting connected components
"""

from typing import Any, List, Dict, Set


def dfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform DFS traversal (iterative) from a starting vertex.

    Steps:
        1. Push start vertex onto stack
        2. While stack is not empty:
           a. Pop a vertex
           b. If not visited, mark visited and process it
           c. Push all unvisited neighbors onto stack
    """
    visited: Set[Any] = set()
    stack: List[Any] = [start]
    result: List[Any] = []

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # Push neighbors in reverse order so we visit in original order
            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return result


def dfs_recursive(graph: Dict[Any, List[Any]], start: Any,
                   visited: Set[Any] = None) -> List[Any]:
    """
    Perform DFS traversal (recursive).

    The recursive version naturally uses the call stack.
    """
    if visited is None:
        visited = set()

    visited.add(start)
    result = [start]

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result


def has_cycle(graph: Dict[Any, List[Any]], directed: bool = True) -> bool:
    """
    Detect if a graph contains a cycle.

    For directed graphs: uses DFS with three states (white/gray/black).
    For undirected graphs: checks if we visit a node that's already visited
                           and is not the parent.
    """
    if directed:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {v: WHITE for v in graph}

        def _dfs(v):
            color[v] = GRAY
            for neighbor in graph.get(v, []):
                if color.get(neighbor, WHITE) == GRAY:
                    return True  # Back edge found → cycle!
                if color.get(neighbor, WHITE) == WHITE and _dfs(neighbor):
                    return True
            color[v] = BLACK
            return False

        return any(_dfs(v) for v in graph if color[v] == WHITE)
    else:
        visited: Set[Any] = set()

        def _dfs_undirected(v, parent):
            visited.add(v)
            for neighbor in graph.get(v, []):
                if neighbor not in visited:
                    if _dfs_undirected(neighbor, v):
                        return True
                elif neighbor != parent:
                    return True
            return False

        return any(
            _dfs_undirected(v, None)
            for v in graph if v not in visited
        )


def dfs_traced(graph: Dict[Any, List[Any]], start: Any) -> dict:
    """DFS with step trace for visualization."""
    visited: Set[Any] = set()
    stack: List[Any] = [start]
    result: List[Any] = []
    steps = [{"type": "start", "vertex": start, "stack": list(stack)}]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            steps.append({"type": "visit", "vertex": vertex, "stack": list(stack)})

            for neighbor in reversed(graph.get(vertex, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    steps.append({"type": "push", "vertex": neighbor,
                                  "from": vertex, "stack": list(stack)})

    steps.append({"type": "done", "result": result})
    return {"result": result, "steps": steps}
