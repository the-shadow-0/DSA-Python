"""
Array Operations
=================

Arrays are the simplest data structure — a contiguous block of memory
storing elements of the same type, accessed by index.

Real-world usage:
    - Image pixel data
    - Sensor readings
    - Stock price histories

Time Complexities:
    Access:    O(1)
    Search:    O(n)
    Insert:    O(n)  — must shift elements
    Delete:    O(n)  — must shift elements
    Append:    O(1)  amortized (Python list)
"""

from typing import List, Any, Optional


def array_insert(arr: List[Any], index: int, value: Any) -> List[Any]:
    """
    Insert a value at a specific index, shifting elements right.

    Time Complexity:  O(n) — must shift elements after index
    Space Complexity: O(1) — in-place modification

    Steps:
        1. Validate the index
        2. Shift all elements from index onward one position right
        3. Place the new value at the index
    """
    # Step 1: Validate index
    if index < 0 or index > len(arr):
        raise IndexError(f"Index {index} out of range for array of length {len(arr)}")

    # Step 2: Append a placeholder and shift elements right
    arr.append(None)
    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]

    # Step 3: Insert the value
    arr[index] = value
    return arr


def array_delete(arr: List[Any], index: int) -> Any:
    """
    Delete element at index, shifting elements left.

    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    if index < 0 or index >= len(arr):
        raise IndexError(f"Index {index} out of range")

    removed = arr[index]

    # Shift elements left to fill the gap
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]

    arr.pop()  # Remove the duplicate last element
    return removed


def array_search(arr: List[Any], target: Any) -> int:
    """
    Linear search — scan every element until found.

    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def array_reverse(arr: List[Any]) -> List[Any]:
    """
    Reverse array in-place using two pointers.

    Time Complexity:  O(n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        # Swap elements at left and right pointers
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def two_sum(arr: List[int], target: int) -> Optional[tuple]:
    """
    Find two numbers that add up to target using a hash map.

    Time Complexity:  O(n)
    Space Complexity: O(n)

    Real-world: Finding complementary items in inventory.
    """
    seen = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i

    return None
