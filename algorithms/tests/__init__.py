"""Tests for algorithm implementations."""

import pytest
from algorithms.sorting.bubble_sort import bubble_sort
from algorithms.sorting.selection_sort import selection_sort
from algorithms.sorting.insertion_sort import insertion_sort
from algorithms.sorting.merge_sort import merge_sort
from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.heap_sort import heap_sort


class TestSorting:
    """Test all sorting algorithms with the same test cases."""

    ALGORITHMS = [bubble_sort, selection_sort, insertion_sort,
                  merge_sort, quick_sort, heap_sort]

    @pytest.mark.parametrize("sort_func", ALGORITHMS,
                             ids=lambda f: f.__name__)
    def test_basic(self, sort_func):
        assert sort_func([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]

    @pytest.mark.parametrize("sort_func", ALGORITHMS,
                             ids=lambda f: f.__name__)
    def test_empty(self, sort_func):
        assert sort_func([]) == []

    @pytest.mark.parametrize("sort_func", ALGORITHMS,
                             ids=lambda f: f.__name__)
    def test_single(self, sort_func):
        assert sort_func([1]) == [1]

    @pytest.mark.parametrize("sort_func", ALGORITHMS,
                             ids=lambda f: f.__name__)
    def test_already_sorted(self, sort_func):
        assert sort_func([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    @pytest.mark.parametrize("sort_func", ALGORITHMS,
                             ids=lambda f: f.__name__)
    def test_reverse_sorted(self, sort_func):
        assert sort_func([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    @pytest.mark.parametrize("sort_func", ALGORITHMS,
                             ids=lambda f: f.__name__)
    def test_duplicates(self, sort_func):
        assert sort_func([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
