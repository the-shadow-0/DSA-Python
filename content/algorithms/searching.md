# Searching Algorithms: Finding the Needle

Searching is the process of finding the position of a specific target element within a collection.

## 1. Linear Search
The simplest possible search. You check every element one by one until you find a match.
- **Requirement**: None.
- **Time Complexity**: `O(n)`
- **When to use**: Unsorted small data.

```python
def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target: return i
    return -1
```

## 2. Binary Search
The most efficient search for sorted data. It works by repeatedly dividing the search interval in half.
- **Requirement**: Data **must be sorted**.
- **Time Complexity**: `O(log n)`
- **When to use**: Large sorted datasets.

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1
```

## Advanced Search: Ternary Search
Similar to Binary Search, but divides the array into **three parts**.
- **Complexity**: `O(log3 n)`
- **Use Case**: Finding the maximum or minimum of a unimodal function.

## Search Performance Comparison
| Algorithm | Best | Average | Worst |
|---|---|---|---|
| Linear | `O(1)` | `O(n)` | `O(n)` |
| Binary | `O(1)` | `O(log n)` | `O(log n)` |

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Searching?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Searching compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Search Variations: Search Variations

### Way 1: Binary Search (Iterative)
```python
def search(arr, x):
    # standard loop implementation...
```

### Way 2: Binary Search (Recursive)
```python
def search(arr, l, r, x):
    # recursive implementation...
```


### Way 3: Exponential Search (for unbounded lists)
```python
i = 1
while i < n and arr[i] <= x: i *= 2
# followed by binary search in [i/2, min(i, n-1)]
```

### Way 4: Interpolation Search (for uniform distributions)
```python
pos = low + ((target-arr[low])*(high-low) // (arr[high]-arr[low]))
```

## 🌍 Real-World Use Case
**Scenario**: Locating specific offsets in large binary files.
*Why it matters*: Real-world systems prioritize either maintenance simplicity or raw execution speed depending on scale.

