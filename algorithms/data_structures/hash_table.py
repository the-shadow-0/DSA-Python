"""
Hash Table
===========

A hash table maps keys to values using a hash function.
It provides near-constant time lookups, inserts, and deletes.

Real-world usage:
    - Database indexing
    - Caching (Redis, Memcached)
    - Symbol tables in compilers
    - Python dictionaries

Time Complexities (average):
    Insert:  O(1)
    Lookup:  O(1)
    Delete:  O(1)
    Worst case (hash collisions): O(n)
"""

from typing import Any, Optional, List, Tuple


class HashTable:
    """
    Hash Table implementation using separate chaining for collision resolution.

    Each bucket is a list of (key, value) pairs.

    Steps of how hashing works:
        1. Compute hash of the key → integer
        2. Map hash to bucket index → hash % table_size
        3. Store (key, value) in that bucket
        4. On collision, chain entries in the same bucket
    """

    def __init__(self, capacity: int = 16):
        self.capacity = capacity
        self.size = 0
        # Each bucket is a list of (key, value) pairs
        self.buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(capacity)]
        self.load_factor_threshold = 0.75

    def _hash(self, key: Any) -> int:
        """
        Compute the bucket index for a given key.

        Time Complexity: O(1)
        """
        return hash(key) % self.capacity

    def put(self, key: Any, value: Any) -> None:
        """
        Insert or update a key-value pair.

        Time Complexity:  O(1) average, O(n) worst case
        Space Complexity: O(1)

        Steps:
            1. Hash the key to find the bucket
            2. Check if key already exists in bucket → update
            3. If not found, append new (key, value) pair
            4. Resize if load factor exceeds threshold
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        # Step 2: Check for existing key
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return

        # Step 3: Key not found — insert new entry
        bucket.append((key, value))
        self.size += 1

        # Step 4: Resize if load factor is too high
        if self.size / self.capacity > self.load_factor_threshold:
            self._resize()

    def get(self, key: Any) -> Optional[Any]:
        """
        Retrieve a value by key.

        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        return None  # Key not found

    def delete(self, key: Any) -> bool:
        """
        Remove a key-value pair.

        Time Complexity: O(1) average
        """
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return True

        return False

    def contains(self, key: Any) -> bool:
        """Check if a key exists. O(1) average."""
        return self.get(key) is not None

    def _resize(self) -> None:
        """
        Double the capacity and rehash all entries.

        This is what keeps the average O(1) performance —
        when the table gets too full, we spread entries out.
        """
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

    def keys(self) -> List[Any]:
        """Return all keys."""
        result = []
        for bucket in self.buckets:
            for k, v in bucket:
                result.append(k)
        return result

    def values(self) -> List[Any]:
        """Return all values."""
        result = []
        for bucket in self.buckets:
            for k, v in bucket:
                result.append(v)
        return result

    def __repr__(self):
        pairs = []
        for bucket in self.buckets:
            for k, v in bucket:
                pairs.append(f"{k}: {v}")
        return "{" + ", ".join(pairs) + "}"

    def __len__(self):
        return self.size
