"""
Trie (Prefix Tree)
====================

A tree-like data structure for efficiently storing and retrieving
strings. Each node represents a character, and paths from root
to marked nodes form complete words.

Real-world usage:
    - Autocomplete / search suggestions
    - Spell checkers
    - IP routing (longest prefix match)
    - Phone dictionaries (T9 input)

Time Complexities (for a word of length m):
    Insert: O(m)
    Search: O(m)
    Prefix: O(m)

Space Complexity: O(n × m) where n = words, m = avg word length
"""

from typing import List, Optional


class TrieNode:
    """A node in the Trie."""

    def __init__(self):
        self.children = {}       # char → TrieNode
        self.is_end_of_word = False
        self.word_count = 0      # Number of words ending here


class Trie:
    """
    Prefix Tree implementation.

    Supports: insert, search, starts_with, autocomplete, delete.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Time Complexity: O(m) where m = len(word)

        Steps:
            1. Start at root
            2. For each character, follow or create child node
            3. Mark the last node as end of word
        """
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.is_end_of_word = True
        node.word_count += 1

    def search(self, word: str) -> bool:
        """
        Check if a word exists in the Trie.

        Time Complexity: O(m)
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word starts with the given prefix.

        Time Complexity: O(m)
        """
        return self._find_node(prefix) is not None

    def autocomplete(self, prefix: str, max_results: int = 10) -> List[str]:
        """
        Return all words that start with the given prefix.

        Time Complexity: O(m + k) where k = number of matching words
        """
        node = self._find_node(prefix)
        if node is None:
            return []

        results = []
        self._collect_words(node, prefix, results, max_results)
        return results

    def delete(self, word: str) -> bool:
        """Delete a word from the Trie. Returns True if word was found and deleted."""
        return self._delete_recursive(self.root, word, 0)

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        """Find the node corresponding to the end of a prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def _collect_words(self, node: TrieNode, prefix: str,
                        results: List[str], max_results: int) -> None:
        """Collect all words under a node using DFS."""
        if len(results) >= max_results:
            return

        if node.is_end_of_word:
            results.append(prefix)

        for char in sorted(node.children.keys()):
            self._collect_words(node.children[char], prefix + char,
                                results, max_results)

    def _delete_recursive(self, node: TrieNode, word: str, depth: int) -> bool:
        """Recursively delete a word, cleaning up empty nodes."""
        if depth == len(word):
            if not node.is_end_of_word:
                return False
            node.is_end_of_word = False
            node.word_count -= 1
            return len(node.children) == 0  # Can delete node if no children

        char = word[depth]
        if char not in node.children:
            return False

        should_delete = self._delete_recursive(node.children[char], word, depth + 1)

        if should_delete:
            del node.children[char]
            return not node.is_end_of_word and len(node.children) == 0

        return False
