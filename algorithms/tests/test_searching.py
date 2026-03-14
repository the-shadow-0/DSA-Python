"""Tests for searching algorithms."""

from algorithms.searching.linear_search import linear_search
from algorithms.searching.binary_search import binary_search, binary_search_recursive


class TestLinearSearch:
    def test_found(self):
        assert linear_search([10, 20, 30, 40], 30) == 2

    def test_not_found(self):
        assert linear_search([10, 20, 30], 99) == -1

    def test_empty(self):
        assert linear_search([], 1) == -1


class TestBinarySearch:
    def test_found(self):
        assert binary_search([1, 3, 5, 7, 9], 5) == 2

    def test_not_found(self):
        assert binary_search([1, 3, 5, 7, 9], 4) == -1

    def test_recursive(self):
        assert binary_search_recursive([1, 3, 5, 7, 9], 7) == 3

    def test_first_element(self):
        assert binary_search([1, 3, 5], 1) == 0

    def test_last_element(self):
        assert binary_search([1, 3, 5], 5) == 2
