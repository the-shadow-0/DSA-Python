# Tries: The Prefix Tree

A Trie (pronounced "try") is a specialized tree-like data structure used to store a dynamic set of strings, where the keys are usually strings.

## How it Works
- Each node represents a single character of a string.
- The path from the root to a node represents a prefix of strings stored in the trie.
- Nodes have an `isEndOfWord` boolean to mark where a word finishes.

## Performance
- **Insert**: `O(L)` where L is the length of the string.
- **Search**: `O(L)`.
- **Complexity**: Independent of the number of strings! It only depends on the length of the string you're looking for.

## Real-world Applications
1. **Autocomplete**: Predicting the next characters as you type.
2. **Spell Checkers**: Checking if a string exists in a dictionary.
3. **IP Routing**: Longest prefix matching for routing tables.

## Python Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
```

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Tries?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Tries compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Trie (Prefix Tree): Trie (Prefix Tree)

### Way 1: Nested Dictionary
```python
trie = {}; curr = trie; for char in word: curr = curr.setdefault(char, {})
```

### Way 2: Class-based Nodes
```python
class TrieNode: def __init__(self): self.children = {}
```


### Way 3: Compact Trie (Radix Tree style)
```python
# Compress chains of single-child nodes into one edge
class Node: def __init__(self, prefix): self.prefix = prefix
```

### Way 4: Bitwise Trie (Fast bit routing)
```python
# Index keys by their binary representation levels
node = root; for bit in key_bits: node = node.child[bit]
```

## 🌍 Real-World Use Case
**Scenario**: Autocomplete engines and IP routing tables.
*Why it matters*: Choosing the right implementation balances cognitive load with technical performance.

