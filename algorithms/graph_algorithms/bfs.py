"""
Breadth-First Search (BFS)
===========================

Explores a graph level by level — visits all neighbors of a node
before moving to the next level.

Uses a QUEUE (FIFO) to track which nodes to visit next.

Time Complexity:  O(V + E)
Space Complexity: O(V)

Real-world:
    - Shortest path in unweighted graphs
    - Social network friend suggestions ("people 2 hops away")
    - Web crawlers
    - GPS navigation (unweighted)
"""

from typing import Any, List, Dict, Set, Optional
from collections import deque


def bfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform BFS traversal from a starting vertex.

    Args:
        graph: Adjacency list {vertex: [neighbor1, neighbor2, ...]}
        start: Starting vertex.

    Returns:
        List of vertices in BFS order.

    Steps:
        1. Add start vertex to queue and mark as visited
        2. While queue is not empty:
           a. Dequeue a vertex
           b. Process it (add to result)
           c. Enqueue all unvisited neighbors
    """
    visited: Set[Any] = set()
    queue: deque = deque([start])
    result: List[Any] = []

    visited.add(start)

    while queue:
        # Step 2a: Dequeue the front vertex
        vertex = queue.popleft()
        # Step 2b: Process it
        result.append(vertex)

        # Step 2c: Explore all unvisited neighbors
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def bfs_shortest_path(graph: Dict[Any, List[Any]],
                       start: Any, end: Any) -> Optional[List[Any]]:
    """
    Find the shortest path between two vertices using BFS.

    BFS guarantees the shortest path in an unweighted graph because
    it explores nodes in order of distance from the start.

    Returns:
        List of vertices in the shortest path, or None if no path exists.
    """
    if start == end:
        return [start]

    visited: Set[Any] = {start}
    queue: deque = deque([(start, [start])])

    while queue:
        vertex, path = queue.popleft()

        for neighbor in graph.get(vertex, []):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # No path found


def bfs_traced(graph: Dict[Any, List[Any]], start: Any) -> dict:
    """BFS with step trace for visualization."""
    visited: Set[Any] = set()
    queue: deque = deque([start])
    result: List[Any] = []
    steps = []

    visited.add(start)
    steps.append({"type": "start", "vertex": start, "queue": list(queue)})

    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        steps.append({"type": "visit", "vertex": vertex, "queue": list(queue)})

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                steps.append({"type": "enqueue", "vertex": neighbor,
                              "from": vertex, "queue": list(queue)})

    steps.append({"type": "done", "result": result})
    return {"result": result, "steps": steps}
