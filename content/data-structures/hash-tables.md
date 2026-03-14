# Hash Tables: Collisions and Cryptography

Python's dictionaries are arguably the most optimized hash maps in software engineering.

## How Hashing Works
1. `hash(key)`: Converts a key into a large integer.
2. `index = hash % table_size`.

## Collision Resolution: Python's Way
Python uses **Open Addressing** with a specific probing sequence.
- Instead of just checking `index + 1`, it uses a sophisticated formula to jump around the array to find an empty slot.
- This prevents "clustering" where long chains of items form.

## Load Factor and Resizing
- **Load Factor**: Number of items / Table Size.
- When the table is 2/3 full, Python doubles the size.
- **Why?** At 100% full, finding an empty slot becomes `O(n)`. Maintaining a low load factor keeps it `O(1)`.

## Immutable Keys
Only **hashable** objects can be keys.
- **Yes**: `int`, `str`, `tuple` (if all items are hashable).
- **No**: `list`, `dict`, `set`.
**Why?** If a key's value changes, its hash changes, and you'd never find it again in the table!

## Vulnerability: Hash Flooding
Attackers can send keys that all hash to the same value, forcing `O(n)` performance and crashing servers (Denial of Service). Python mitigates this by "salting" hashes with a random seed on startup.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Hash Tables?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Hash Tables compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Hash Table Logic: Hash Table Logic

### Way 1: Standard O(1) Dictionary
```python
cache = {'key': 'val'}
val = cache.get('key')
```

### Way 2: LRU Caching via `OrderedDict`
```python
from collections import OrderedDict
cache = OrderedDict()
cache['a'] = 1
cache.move_to_end('a')
```


### Way 3: LRU Cache via `@lru_cache` decorator
```python
from functools import lru_cache
@lru_cache(maxsize=128)
def get_expensive_resource(id): return ...
```

### Way 4: Counter for Frequency (optimized dict)
```python
from collections import Counter
counts = Counter(['a', 'b', 'a'])
# prints {'a': 2, 'b': 1}
```

## 🌍 Real-World Use Case
**Scenario**: Session management and API response caching.
*Why it matters*: Real-world systems prioritize either maintenance simplicity or raw execution speed depending on scale.

