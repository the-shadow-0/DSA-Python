"""Tests for sorting algorithms."""

import pytest
from algorithms.sorting.bubble_sort import bubble_sort, bubble_sort_traced
from algorithms.sorting.merge_sort import merge_sort, merge_sort_traced
from algorithms.sorting.quick_sort import quick_sort, quick_sort_traced


class TestBubbleSortTraced:
    def test_traced_produces_steps(self):
        result = bubble_sort_traced([3, 1, 2])
        assert result["sorted"] == [1, 2, 3]
        assert len(result["steps"]) > 0
        assert result["steps"][-1]["type"] == "done"


class TestMergeSortTraced:
    def test_traced_produces_steps(self):
        result = merge_sort_traced([3, 1, 4, 1, 5])
        assert result["sorted"] == [1, 1, 3, 4, 5]
        assert any(s["type"] == "split" for s in result["steps"])
        assert any(s["type"] == "merge" for s in result["steps"])


class TestQuickSortTraced:
    def test_traced_produces_steps(self):
        result = quick_sort_traced([3, 1, 4, 1, 5])
        assert result["sorted"] == [1, 1, 3, 4, 5]
        assert any(s["type"] == "pivot" for s in result["steps"])
