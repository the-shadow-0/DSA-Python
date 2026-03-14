"""
Fibonacci — Dynamic Programming
=================================

The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
Each number is the sum of the two preceding numbers.

This is the classic example for comparing:
    1. Naive recursion    → O(2^n)
    2. Memoization (top-down DP)  → O(n)
    3. Tabulation (bottom-up DP)  → O(n)
    4. Space-optimized    → O(n) time, O(1) space
"""

from typing import Dict


def fibonacci_recursive(n: int) -> int:
    """
    Naive recursive Fibonacci.

    Time Complexity:  O(2^n) — exponential!
    Space Complexity: O(n) — recursion stack

    Problem: We recalculate the same subproblems many times.
    Example: fib(5) calls fib(3) twice, fib(2) three times, etc.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoized(n: int, memo: Dict[int, int] = None) -> int:
    """
    Fibonacci with memoization (top-down DP).

    Time Complexity:  O(n) — each subproblem solved once
    Space Complexity: O(n) — memo + recursion stack

    Key insight: Store results of subproblems to avoid recalculation.
    This is "top-down" because we start from the big problem and work down.
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1

    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


def fibonacci_tabulation(n: int) -> int:
    """
    Fibonacci with tabulation (bottom-up DP).

    Time Complexity:  O(n)
    Space Complexity: O(n) — table

    Key insight: Build solutions from smallest subproblems upward.
    This is "bottom-up" because we start from base cases and build up.

    Steps:
        1. Create a table of size n+1
        2. Fill base cases: dp[0] = 0, dp[1] = 1
        3. Fill each cell: dp[i] = dp[i-1] + dp[i-2]
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fibonacci_optimized(n: int) -> int:
    """
    Space-optimized Fibonacci.

    Time Complexity:  O(n)
    Space Complexity: O(1) — only two variables!

    Key insight: We only need the last two values, not the entire table.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1


def fibonacci_traced(n: int) -> dict:
    """Fibonacci tabulation with step trace for visualization."""
    if n <= 0:
        return {"result": 0, "steps": [{"index": 0, "value": 0}]}

    dp = [0] * (n + 1)
    dp[1] = 1
    steps = [
        {"index": 0, "value": 0, "type": "base"},
        {"index": 1, "value": 1, "type": "base"},
    ]

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        steps.append({
            "index": i, "value": dp[i], "type": "compute",
            "from": [i - 1, i - 2],
            "values": [dp[i - 1], dp[i - 2]],
            "table": list(dp[:i + 1])
        })

    return {"result": dp[n], "steps": steps}
