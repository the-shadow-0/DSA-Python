"""Tests for dynamic programming algorithms."""

from algorithms.dynamic_programming.fibonacci import (
    fibonacci_recursive, fibonacci_memoized,
    fibonacci_tabulation, fibonacci_optimized
)
from algorithms.dynamic_programming.knapsack import knapsack, knapsack_with_items
from algorithms.dynamic_programming.longest_common_subsequence import lcs_length, lcs_string
from algorithms.dynamic_programming.coin_change import coin_change, coin_change_combinations


class TestFibonacci:
    def test_all_methods_agree(self):
        for n in range(15):
            expected = fibonacci_tabulation(n)
            assert fibonacci_recursive(n) == expected
            assert fibonacci_memoized(n) == expected
            assert fibonacci_optimized(n) == expected

    def test_known_values(self):
        assert fibonacci_tabulation(0) == 0
        assert fibonacci_tabulation(1) == 1
        assert fibonacci_tabulation(10) == 55
        assert fibonacci_tabulation(20) == 6765


class TestKnapsack:
    def test_basic(self):
        weights = [2, 3, 4, 5]
        values = [3, 4, 5, 6]
        assert knapsack(weights, values, 5) == 7  # Items 0+1

    def test_with_items(self):
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        max_val, items = knapsack_with_items(weights, values, 7)
        assert max_val == 9  # Items 1+2 (4+5)


class TestLCS:
    def test_length(self):
        assert lcs_length("ABCBDAB", "BDCAB") == 4

    def test_string(self):
        result = lcs_string("ABCBDAB", "BDCAB")
        assert len(result) == 4

    def test_no_common(self):
        assert lcs_length("ABC", "XYZ") == 0

    def test_identical(self):
        assert lcs_length("ABC", "ABC") == 3


class TestCoinChange:
    def test_basic(self):
        assert coin_change([1, 5, 10, 25], 30) == 2  # 25 + 5

    def test_impossible(self):
        assert coin_change([2], 3) == -1

    def test_zero(self):
        assert coin_change([1, 2, 5], 0) == 0

    def test_combinations(self):
        assert coin_change_combinations([1, 2, 5], 5) == 4  # {5}, {2+2+1}, {2+1+1+1}, {1+1+1+1+1}
