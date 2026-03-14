"""
Binary Search Tree (BST)
=========================

A BST is a tree where for each node:
    - Left child's value < node's value
    - Right child's value > node's value

This property enables efficient searching — similar to binary search.

Real-world usage:
    - Database indexing (B-trees are BST variants)
    - File system organization
    - Auto-complete suggestions

Time Complexities (average / balanced):
    Search:  O(log n)
    Insert:  O(log n)
    Delete:  O(log n)
    Worst (skewed): O(n)
"""

from typing import Any, Optional, List


class TreeNode:
    """A single node in a binary tree."""

    def __init__(self, value: Any):
        self.value = value
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

    def __repr__(self):
        return f"TreeNode({self.value})"


class BinarySearchTree:
    """
    Binary Search Tree with insert, search, delete, and traversals.
    """

    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, value: Any) -> None:
        """
        Insert a value into the BST.

        Time Complexity:  O(log n) average, O(n) worst
        Space Complexity: O(log n) — recursion stack

        Steps:
            1. If tree is empty, new node becomes root
            2. Compare value with current node
            3. Go left if smaller, right if larger
            4. Insert at the correct leaf position
        """
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value: Any) -> TreeNode:
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
        # Duplicate values are ignored
        return node

    def search(self, value: Any) -> bool:
        """
        Search for a value in the BST.

        Time Complexity:  O(log n) average
        Space Complexity: O(log n) — recursion stack

        Steps:
            1. Compare target with current node
            2. If equal → found!
            3. If smaller → search left subtree
            4. If larger → search right subtree
            5. If node is None → not found
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node: Optional[TreeNode], value: Any) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def delete(self, value: Any) -> None:
        """
        Delete a value from the BST.

        Time Complexity:  O(log n) average

        Three cases:
            1. Node has no children → simply remove it
            2. Node has one child → replace with child
            3. Node has two children → replace with in-order successor
        """
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node: Optional[TreeNode], value: Any) -> Optional[TreeNode]:
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Found the node to delete
            # Case 1 & 2: No child or one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Case 3: Two children — find in-order successor
            successor = self._find_min(node.right)
            node.value = successor.value
            node.right = self._delete_recursive(node.right, successor.value)

        return node

    def _find_min(self, node: TreeNode) -> TreeNode:
        """Find the minimum value node (leftmost node)."""
        while node.left:
            node = node.left
        return node

    # ──────────────────────────────────────────
    # Tree Traversals
    # ──────────────────────────────────────────

    def inorder(self) -> List[Any]:
        """
        In-order traversal: Left → Root → Right.
        Returns elements in sorted order.

        Time Complexity: O(n)
        """
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[TreeNode], result: List):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def preorder(self) -> List[Any]:
        """
        Pre-order traversal: Root → Left → Right.
        Useful for copying the tree.
        """
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node: Optional[TreeNode], result: List):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self) -> List[Any]:
        """
        Post-order traversal: Left → Right → Root.
        Useful for deleting the tree.
        """
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node: Optional[TreeNode], result: List):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

    def level_order(self) -> List[List[Any]]:
        """
        Level-order (BFS) traversal.
        Returns elements level by level.

        Time Complexity: O(n)
        """
        if not self.root:
            return []

        from collections import deque
        result = []
        queue = deque([self.root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result

    def height(self) -> int:
        """Get the height of the tree."""
        return self._height(self.root)

    def _height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))
