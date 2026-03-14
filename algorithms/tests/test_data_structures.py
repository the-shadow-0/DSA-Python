"""Tests for data structure implementations."""

import pytest
from algorithms.data_structures.linked_list import LinkedList
from algorithms.data_structures.stack import Stack, is_valid_parentheses
from algorithms.data_structures.queue_ds import Queue, PriorityQueue
from algorithms.data_structures.hash_table import HashTable
from algorithms.data_structures.bst import BinarySearchTree
from algorithms.data_structures.heap import MinHeap, heapify


class TestLinkedList:
    def test_insert_and_traverse(self):
        ll = LinkedList()
        ll.insert_tail(1)
        ll.insert_tail(2)
        ll.insert_tail(3)
        assert ll.to_list() == [1, 2, 3]

    def test_insert_head(self):
        ll = LinkedList()
        ll.insert_head(3)
        ll.insert_head(2)
        ll.insert_head(1)
        assert ll.to_list() == [1, 2, 3]

    def test_delete(self):
        ll = LinkedList()
        ll.insert_tail(1)
        ll.insert_tail(2)
        ll.insert_tail(3)
        ll.delete(2)
        assert ll.to_list() == [1, 3]

    def test_search(self):
        ll = LinkedList()
        ll.insert_tail(10)
        ll.insert_tail(20)
        assert ll.search(20) == 1
        assert ll.search(99) is None

    def test_reverse(self):
        ll = LinkedList()
        for v in [1, 2, 3, 4]:
            ll.insert_tail(v)
        ll.reverse()
        assert ll.to_list() == [4, 3, 2, 1]


class TestStack:
    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.pop() == 3
        assert s.pop() == 2

    def test_peek(self):
        s = Stack()
        s.push(42)
        assert s.peek() == 42
        assert s.size == 1

    def test_empty(self):
        s = Stack()
        assert s.is_empty()
        with pytest.raises(IndexError):
            s.pop()

    def test_valid_parentheses(self):
        assert is_valid_parentheses("({[]})") is True
        assert is_valid_parentheses("([)]") is False
        assert is_valid_parentheses("") is True
        assert is_valid_parentheses("(") is False


class TestQueue:
    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert q.dequeue() == 1
        assert q.dequeue() == 2

    def test_empty(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.dequeue()


class TestPriorityQueue:
    def test_priority(self):
        pq = PriorityQueue()
        pq.enqueue("low", 3)
        pq.enqueue("high", 1)
        pq.enqueue("medium", 2)
        assert pq.dequeue() == "high"
        assert pq.dequeue() == "medium"


class TestHashTable:
    def test_put_get(self):
        ht = HashTable()
        ht.put("name", "Alice")
        ht.put("age", 30)
        assert ht.get("name") == "Alice"
        assert ht.get("age") == 30
        assert ht.get("missing") is None

    def test_update(self):
        ht = HashTable()
        ht.put("key", "old")
        ht.put("key", "new")
        assert ht.get("key") == "new"

    def test_delete(self):
        ht = HashTable()
        ht.put("key", "value")
        assert ht.delete("key") is True
        assert ht.get("key") is None

    def test_resize(self):
        ht = HashTable(capacity=4)
        for i in range(20):
            ht.put(f"key{i}", i)
        assert len(ht) == 20
        assert ht.get("key15") == 15


class TestBST:
    def test_insert_and_search(self):
        bst = BinarySearchTree()
        for val in [5, 3, 7, 1, 4]:
            bst.insert(val)
        assert bst.search(4) is True
        assert bst.search(6) is False

    def test_inorder(self):
        bst = BinarySearchTree()
        for val in [5, 3, 7, 1, 4, 6, 8]:
            bst.insert(val)
        assert bst.inorder() == [1, 3, 4, 5, 6, 7, 8]

    def test_delete(self):
        bst = BinarySearchTree()
        for val in [5, 3, 7]:
            bst.insert(val)
        bst.delete(3)
        assert bst.search(3) is False
        assert bst.inorder() == [5, 7]

    def test_level_order(self):
        bst = BinarySearchTree()
        for val in [5, 3, 7]:
            bst.insert(val)
        assert bst.level_order() == [[5], [3, 7]]


class TestMinHeap:
    def test_insert_extract(self):
        heap = MinHeap()
        for val in [5, 3, 8, 1, 2]:
            heap.insert(val)
        assert heap.extract_min() == 1
        assert heap.extract_min() == 2
        assert heap.extract_min() == 3

    def test_peek(self):
        heap = MinHeap()
        heap.insert(10)
        heap.insert(5)
        assert heap.peek() == 5

    def test_heapify(self):
        arr = [5, 3, 8, 1, 2]
        result = heapify(arr)
        assert result[0] == 1  # Min at root
