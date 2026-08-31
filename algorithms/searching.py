"""
Algorithm Arena - Searching Algorithms
=======================================
Classic search algorithms with clean implementations.
"""

from typing import List, TypeVar, Optional

T = TypeVar("T", int, float)


def linear_search(arr: List[T], target: T) -> Optional[int]:
    """Linear Search - O(n). Scans the list sequentially.
    Returns the index of target, or None if not found.
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return None


def binary_search(arr: List[T], target: T) -> Optional[int]:
    """Binary Search - O(log n). Requires sorted input.
    Returns the index of target, or None if not found.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


def binary_search_recursive(arr: List[T], target: T) -> Optional[int]:
    """Binary Search (recursive) - O(log n). Requires sorted input."""
    return _bs_recursive(arr, target, 0, len(arr) - 1)


def _bs_recursive(arr: List[T], target: T, low: int, high: int) -> Optional[int]:
    if low > high:
        return None
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return _bs_recursive(arr, target, mid + 1, high)
    else:
        return _bs_recursive(arr, target, low, mid - 1)


def jump_search(arr: List[T], target: T) -> Optional[int]:
    """Jump Search - O(sqrt(n)). Requires sorted input.
    Jumps ahead by sqrt(n) then linear-scans the block.
    """
    import math
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return None
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return None
    if arr[prev] == target:
        return prev
    return None


def exponential_search(arr: List[T], target: T) -> Optional[int]:
    """Exponential Search - O(log n). Requires sorted input.
    Doubles the range until target is bounded, then binary searches.
    """
    if not arr:
        return None
    if arr[0] == target:
        return 0
    i = 1
    n = len(arr)
    while i < n and arr[i] <= target:
        i *= 2
    result = binary_search(arr[i // 2:min(i, n)], target)
    if result is not None:
        return i // 2 + result
    return None


SEARCH_ALGORITHMS = {
    "linear": linear_search,
    "binary": binary_search,
    "binary_recursive": binary_search_recursive,
    "jump": jump_search,
    "exponential": exponential_search,
}
