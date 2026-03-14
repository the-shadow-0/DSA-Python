"""
0/1 Knapsack Problem
=====================

Given a set of items, each with a weight and value, determine which items
to include in a collection so that the total weight ≤ capacity and total
value is maximized.

"0/1" means each item can be either taken (1) or left (0) — no fractions.

Time Complexity:  O(n × W)  where n = items, W = capacity
Space Complexity: O(n × W)

Real-world:
    - Resource allocation (budget optimization)
    - Cargo loading
    - Portfolio optimization
"""

from typing import List, Tuple


def knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Solve 0/1 knapsack using dynamic programming (tabulation).

    Args:
        weights: Weight of each item.
        values:  Value of each item.
        capacity: Maximum weight capacity.

    Returns:
        Maximum achievable value.

    Steps:
        1. Create dp table: dp[i][w] = max value using first i items with capacity w
        2. For each item, decide: take it or skip it
           - Skip: dp[i][w] = dp[i-1][w]
           - Take: dp[i][w] = dp[i-1][w - weight[i]] + value[i]  (if weight fits)
           - Choose the maximum of the two
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Option 1: Skip this item
            dp[i][w] = dp[i - 1][w]

            # Option 2: Take this item (if it fits)
            if weights[i - 1] <= w:
                take_value = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], take_value)

    return dp[n][capacity]


def knapsack_with_items(weights: List[int], values: List[int],
                         capacity: int) -> Tuple[int, List[int]]:
    """
    Knapsack that also returns which items to take.

    Returns:
        (max_value, [indices of selected items])
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                take_value = dp[i - 1][w - weights[i - 1]] + values[i - 1]
                dp[i][w] = max(dp[i][w], take_value)

    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], sorted(selected)
