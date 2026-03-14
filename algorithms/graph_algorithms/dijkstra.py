"""
Dijkstra's Shortest Path Algorithm
====================================

Finds the shortest path from a source vertex to all other vertices
in a weighted graph with non-negative edge weights.

Uses a priority queue (min-heap) to always process the closest vertex next.

Time Complexity:  O((V + E) log V) with a binary heap
Space Complexity: O(V)

Real-world:
    - GPS navigation (shortest route)
    - Network routing protocols (OSPF)
    - Airline flight scheduling
"""

from typing import Any, Dict, List, Tuple, Optional
import heapq


def dijkstra(graph: Dict[Any, List[Tuple[Any, float]]],
             start: Any) -> Dict[Any, float]:
    """
    Compute shortest distances from start to all reachable vertices.

    Args:
        graph: Adjacency list {vertex: [(neighbor, weight), ...]}
        start: Source vertex.

    Returns:
        Dictionary of {vertex: shortest_distance}.

    Steps:
        1. Initialize distances: start = 0, all others = infinity
        2. Add start to priority queue
        3. While queue is not empty:
           a. Pop vertex with smallest distance
           b. For each neighbor, calculate new distance via this vertex
           c. If new distance is shorter, update and add to queue
    """
    # Step 1: Initialize distances
    distances: Dict[Any, float] = {start: 0}
    priority_queue: List[Tuple[float, Any]] = [(0, start)]
    visited: set = set()

    while priority_queue:
        # Step 3a: Get closest unvisited vertex
        current_dist, current = heapq.heappop(priority_queue)

        if current in visited:
            continue
        visited.add(current)

        # Step 3b: Check all neighbors
        for neighbor, weight in graph.get(current, []):
            new_dist = current_dist + weight

            # Step 3c: If we found a shorter path, update
            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return distances


def dijkstra_with_path(graph: Dict[Any, List[Tuple[Any, float]]],
                        start: Any, end: Any) -> Tuple[float, List[Any]]:
    """
    Find shortest path and distance between two vertices.

    Returns:
        (distance, [path]) or (inf, []) if no path exists.
    """
    distances = {start: 0}
    previous: Dict[Any, Optional[Any]] = {start: None}
    priority_queue = [(0, start)]
    visited: set = set()

    while priority_queue:
        current_dist, current = heapq.heappop(priority_queue)

        if current in visited:
            continue
        visited.add(current)

        if current == end:
            # Reconstruct path
            path = []
            node = end
            while node is not None:
                path.append(node)
                node = previous.get(node)
            return current_dist, list(reversed(path))

        for neighbor, weight in graph.get(current, []):
            new_dist = current_dist + weight
            if new_dist < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_dist
                previous[neighbor] = current
                heapq.heappush(priority_queue, (new_dist, neighbor))

    return float('inf'), []


def dijkstra_traced(graph: Dict[Any, List[Tuple[Any, float]]],
                     start: Any) -> dict:
    """Dijkstra with step trace for visualization."""
    distances = {start: 0}
    priority_queue = [(0, start)]
    visited: set = set()
    steps = [{"type": "start", "vertex": start, "distances": dict(distances)}]

    while priority_queue:
        current_dist, current = heapq.heappop(priority_queue)

        if current in visited:
            continue
        visited.add(current)
        steps.append({"type": "visit", "vertex": current,
                       "distance": current_dist, "distances": dict(distances)})

        for neighbor, weight in graph.get(current, []):
            new_dist = current_dist + weight
            old_dist = distances.get(neighbor, float('inf'))

            if new_dist < old_dist:
                distances[neighbor] = new_dist
                heapq.heappush(priority_queue, (new_dist, neighbor))
                steps.append({"type": "relax", "from": current,
                              "to": neighbor, "new_dist": new_dist,
                              "old_dist": old_dist if old_dist != float('inf') else "∞",
                              "distances": dict(distances)})

    steps.append({"type": "done", "distances": distances})
    return {"distances": distances, "steps": steps}
