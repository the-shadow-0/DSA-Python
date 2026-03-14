"""
Linear Search
==============

Scan every element until the target is found.
The simplest searching algorithm — no requirements on input order.

Time Complexity:
    Best:    O(1) — target is first element
    Average: O(n)
    Worst:   O(n) — target is last or not present

Space Complexity: O(1)
"""

from typing import List


def linear_search(arr: List[int], target: int) -> int:
    """
    Search for target in arr. Return index or -1.

    Steps:
        1. Start from the first element
        2. Compare each element with target
        3. Return index if found
        4. Return -1 if we reach the end without finding it
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_traced(arr: List[int], target: int) -> dict:
    """Linear search with step trace for visualization."""
    steps = []
    for i in range(len(arr)):
        if arr[i] == target:
            steps.append({"index": i, "value": arr[i], "status": "found"})
            return {"result": i, "steps": steps}
        steps.append({"index": i, "value": arr[i], "status": "checked"})

    return {"result": -1, "steps": steps}
