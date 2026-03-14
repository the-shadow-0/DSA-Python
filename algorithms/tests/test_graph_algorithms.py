"""Tests for graph algorithms."""

from algorithms.graph_algorithms.bfs import bfs, bfs_shortest_path
from algorithms.graph_algorithms.dfs import dfs, has_cycle
from algorithms.graph_algorithms.dijkstra import dijkstra, dijkstra_with_path
from algorithms.graph_algorithms.topological_sort import topological_sort_kahn


SAMPLE_GRAPH = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}


class TestBFS:
    def test_traversal(self):
        result = bfs(SAMPLE_GRAPH, 'A')
        assert result[0] == 'A'
        assert set(result) == {'A', 'B', 'C', 'D', 'E', 'F'}

    def test_shortest_path(self):
        path = bfs_shortest_path(SAMPLE_GRAPH, 'A', 'F')
        assert path is not None
        assert path[0] == 'A'
        assert path[-1] == 'F'
        assert len(path) == 3  # A -> C -> F


class TestDFS:
    def test_traversal(self):
        result = dfs(SAMPLE_GRAPH, 'A')
        assert result[0] == 'A'
        assert set(result) == {'A', 'B', 'C', 'D', 'E', 'F'}

    def test_cycle_detection_directed(self):
        cyclic = {'A': ['B'], 'B': ['C'], 'C': ['A']}
        assert has_cycle(cyclic, directed=True) is True

        acyclic = {'A': ['B'], 'B': ['C'], 'C': []}
        assert has_cycle(acyclic, directed=True) is False


class TestDijkstra:
    def test_shortest_distances(self):
        weighted_graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('C', 2), ('D', 5)],
            'C': [('D', 1)],
            'D': [],
        }
        distances = dijkstra(weighted_graph, 'A')
        assert distances['A'] == 0
        assert distances['B'] == 1
        assert distances['C'] == 3  # A -> B -> C
        assert distances['D'] == 4  # A -> B -> C -> D

    def test_shortest_path(self):
        weighted_graph = {
            'A': [('B', 1), ('C', 4)],
            'B': [('C', 2), ('D', 5)],
            'C': [('D', 1)],
            'D': [],
        }
        dist, path = dijkstra_with_path(weighted_graph, 'A', 'D')
        assert dist == 4
        assert path == ['A', 'B', 'C', 'D']


class TestTopologicalSort:
    def test_basic(self):
        dag = {
            'A': ['C'],
            'B': ['C', 'D'],
            'C': ['E'],
            'D': ['F'],
            'E': ['F'],
            'F': [],
        }
        result = topological_sort_kahn(dag)
        # A and B should come before C; C before E; D and E before F
        assert result.index('A') < result.index('C')
        assert result.index('B') < result.index('C')
        assert result.index('C') < result.index('E')
        assert result.index('E') < result.index('F')
