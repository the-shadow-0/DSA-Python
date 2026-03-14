# Trees: The Hierarchical Structure

A tree is a non-linear data structure that represents hierarchical relationships. It consists of nodes connected by edges.

## Key Terminology
- **Root**: The top node.
- **Child**: A node directly connected from another node above.
- **Parent**: The node above a child node.
- **Leaf**: A node with no children.
- **Height**: The number of edges on the longest path from a node to a leaf.
- **Depth**: The number of edges from the root to the node.

## Binary Tree
A tree where each node has at most **two children** (Left and Right).

### Binary Search Tree (BST)
A binary tree with a special rule:
- Left subtree values < Parent value.
- Right subtree values > Parent value.
**Why?** This allows searching in `O(log n)` time!

## Tree Traversals

1. **Pre-order (N-L-R)**: Root, then children.
2. **In-order (L-N-R)**: Left, Node, Right. (Returns sorted values in a BST).
3. **Post-order (L-R-N)**: Children first, then Node.

## Python Implementation

```python
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
```

## Real-world Applications
1. **File Systems**: Folders and subfolders.
2. **HTML DOM**: The structure of a webpage.
3. **Organized Databases**: Used for fast indexing.
4. **AI Decision Making**: Game trees in chess or tic-tac-toe.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Trees?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Trees compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Tree Traversals: Tree Traversals

### Way 1: Recursive Depth-First (In-order)
```python
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
```

### Way 2: Iterative Breadth-First (Level-order)
```python
def bfs(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```


### Way 3: AVL Tree (Self-balancing)
```python
# Logic involves Left-Rotate and Right-Rotate
def rotate_left(z):
    y = z.right; T2 = y.left; y.left = z; z.right = T2
```

### Way 4: Heap as a Tree (Array Representation)
```python
tree = [None, root, left, right]
# left_child = 2 * i; right_child = 2 * i + 1
```

## 🌍 Real-World Use Case
**Scenario**: XML/HTML parsing and DOM tree manipulation.
*Why it matters*: Real-world systems prioritize either maintenance simplicity or raw execution speed depending on scale.

