"""
Algorithm Arena - Sorting Algorithms
====================================
Clean, documented implementations of classic sorting algorithms.
Each function returns a sorted list and does NOT mutate the input.
"""

from typing import List, TypeVar, Callable

T = TypeVar("T", int, float)


def bubble_sort(arr: List[T]) -> List[T]:
    """Bubble Sort - O(n^2). Repeatedly swaps adjacent out-of-order elements."""
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


def selection_sort(arr: List[T]) -> List[T]:
    """Selection Sort - O(n^2). Selects the minimum from the unsorted portion."""
    a = arr[:]
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr: List[T]) -> List[T]:
    """Insertion Sort - O(n^2), O(n) best case. Builds sorted portion left-to-right."""
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr: List[T]) -> List[T]:
    """Merge Sort - O(n log n). Divide-and-conquer, stable sort."""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[T], right: List[T]) -> List[T]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr: List[T]) -> List[T]:
    """Quick Sort - O(n log n) avg, O(n^2) worst. In-place partition."""
    a = arr[:]
    _quick_sort_helper(a, 0, len(a) - 1)
    return a


def _quick_sort_helper(a: List[T], low: int, high: int) -> None:
    if low < high:
        pivot = _partition(a, low, high)
        _quick_sort_helper(a, low, pivot - 1)
        _quick_sort_helper(a, pivot + 1, high)


def _partition(a: List[T], low: int, high: int) -> int:
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


def heap_sort(arr: List[T]) -> List[T]:
    """Heap Sort - O(n log n). Builds a max-heap then extracts max repeatedly."""
    a = arr[:]
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        _heapify(a, i, 0)
    return a


def _heapify(a: List[T], n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        _heapify(a, n, largest)


ALGORITHMS: dict = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
    "heap": heap_sort,
}
