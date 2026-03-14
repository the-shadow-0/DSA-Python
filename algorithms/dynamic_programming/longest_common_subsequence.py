"""
Longest Common Subsequence (LCS)
==================================

Find the longest subsequence common to two sequences.
A subsequence doesn't have to be contiguous, but must maintain
relative order.

Time Complexity:  O(m × n)
Space Complexity: O(m × n)

Real-world:
    - Git diff / file comparison
    - DNA sequence alignment
    - Spell checking
"""

from typing import List


def lcs_length(text1: str, text2: str) -> int:
    """
    Find the length of the longest common subsequence.

    Steps:
        1. Create dp table: dp[i][j] = LCS length of text1[:i] and text2[:j]
        2. If characters match: dp[i][j] = dp[i-1][j-1] + 1
        3. If not: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_string(text1: str, text2: str) -> str:
    """
    Find the actual LCS string (not just length).

    After building the DP table, backtrack to reconstruct the subsequence.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the actual subsequence
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            result.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(result))
