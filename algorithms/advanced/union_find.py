"""
Union-Find (Disjoint Set Union)
================================

Efficiently tracks elements partitioned into disjoint sets.
Supports two operations:
    - Find: Which set does element x belong to?
    - Union: Merge two sets together.

With path compression + union by rank → nearly O(1) per operation.

Real-world usage:
    - Kruskal's MST algorithm
    - Network connectivity
    - Image segmentation
    - Least common ancestor in trees

Time Complexity:  O(α(n)) per operation (inverse Ackermann — nearly O(1))
Space Complexity: O(n)
"""

from typing import List


class UnionFind:
    """
    Union-Find with path compression and union by rank.
    """

    def __init__(self, n: int):
        """
        Initialize n elements, each in its own set.

        parent[i] = i means i is the root of its set.
        rank[i] = approximate depth of the tree rooted at i.
        """
        self.parent: List[int] = list(range(n))
        self.rank: List[int] = [0] * n
        self.num_components: int = n

    def find(self, x: int) -> int:
        """
        Find the root (representative) of the set containing x.

        Uses path compression: makes every node on the path
        point directly to the root → flattens the tree.

        Time Complexity: O(α(n)) amortized
        """
        if self.parent[x] != x:
            # Path compression: point directly to root
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """
        Merge the sets containing x and y.

        Uses union by rank: attach the shorter tree under the taller one.
        This keeps trees balanced.

        Returns:
            True if x and y were in different sets (merge happened).
            False if they were already in the same set.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in the same set

        # Union by rank: attach smaller tree under larger
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.num_components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if x and y are in the same set. O(α(n))."""
        return self.find(x) == self.find(y)

    @property
    def components(self) -> int:
        """Number of disjoint sets."""
        return self.num_components
