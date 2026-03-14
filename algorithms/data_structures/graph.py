"""
Graph
======

A graph is a set of vertices (nodes) connected by edges.
Graphs can be directed or undirected, weighted or unweighted.

Real-world usage:
    - Social networks (friend connections)
    - Maps and navigation (roads between cities)
    - Internet routing
    - Dependency resolution (package managers)

Representations:
    - Adjacency List: Space O(V + E), best for sparse graphs
    - Adjacency Matrix: Space O(V²), best for dense graphs
"""

from typing import Any, List, Dict, Optional, Set, Tuple
from collections import defaultdict, deque


class Graph:
    """
    Graph implementation using an adjacency list.

    Supports: directed/undirected, weighted/unweighted,
              BFS, DFS, has_cycle, shortest_path.
    """

    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adjacency_list: Dict[Any, List[Tuple[Any, float]]] = defaultdict(list)
        self._vertices: Set[Any] = set()

    def add_vertex(self, vertex: Any) -> None:
        """Add a vertex to the graph. O(1)."""
        self._vertices.add(vertex)
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source: Any, destination: Any, weight: float = 1.0) -> None:
        """
        Add an edge between source and destination.

        Time Complexity: O(1)

        For undirected graphs, adds edge in both directions.
        """
        self._vertices.add(source)
        self._vertices.add(destination)

        self.adjacency_list[source].append((destination, weight))

        if not self.directed:
            self.adjacency_list[destination].append((source, weight))

    def get_neighbors(self, vertex: Any) -> List[Tuple[Any, float]]:
        """Get all neighbors of a vertex with their edge weights."""
        return self.adjacency_list.get(vertex, [])

    @property
    def vertices(self) -> Set[Any]:
        """All vertices in the graph."""
        return self._vertices

    @property
    def num_vertices(self) -> int:
        return len(self._vertices)

    @property
    def num_edges(self) -> int:
        total = sum(len(edges) for edges in self.adjacency_list.values())
        return total if self.directed else total // 2

    def __repr__(self):
        lines = []
        for vertex in sorted(self._vertices, key=str):
            neighbors = [(n, w) for n, w in self.adjacency_list[vertex]]
            lines.append(f"  {vertex} → {neighbors}")
        return "Graph:\n" + "\n".join(lines)
