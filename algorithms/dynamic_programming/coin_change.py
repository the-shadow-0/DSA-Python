"""
Coin Change Problem
====================

Given a set of coin denominations and a target amount,
find the minimum number of coins needed to make that amount.

Time Complexity:  O(amount × len(coins))
Space Complexity: O(amount)

Real-world:
    - Cash register change-making
    - Currency exchange optimization
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Find minimum coins to make the amount.

    Returns -1 if the amount cannot be made.

    Steps:
        1. Create dp table: dp[i] = min coins to make amount i
        2. Base case: dp[0] = 0 (zero coins for zero amount)
        3. For each amount from 1 to target:
           Try every coin. If coin fits, check if using it gives fewer coins.
           dp[i] = min(dp[i], dp[i - coin] + 1)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_combinations(coins: List[int], amount: int) -> int:
    """
    Count the number of ways to make the amount using given coins.

    Unlike the minimum coins problem, here we count ALL combinations.

    Time Complexity:  O(amount × len(coins))
    Space Complexity: O(amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1  # One way to make 0: use no coins

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]
