"""
Tests for Algorithm Arena
=========================
Run with: python -m pytest tests/ -v
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.sorting import ALGORITHMS as SORTING_ALGORITHMS
from algorithms.searching import SEARCH_ALGORITHMS
from algorithms.graph import bfs, dfs, dijkstra, has_cycle


# ---------- Sorting Tests ----------

TEST_ARRAYS = [
    [],
    [1],
    [2, 1],
    [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
    [5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5],
]


def test_sorting_all():
    for name, func in SORTING_ALGORITHMS.items():
        for arr in TEST_ARRAYS:
            result = func(list(arr))
            expected = sorted(arr)
            assert result == expected, f"{name} failed on {arr}: got {result}, expected {expected}"


# ---------- Searching Tests ----------

def test_linear_search():
    arr = [5, 3, 8, 1, 9, 2]
    assert SEARCH_ALGORITHMS["linear"](arr, 8) == 2
    assert SEARCH_ALGORITHMS["linear"](arr, 10) is None


def test_binary_search():
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert SEARCH_ALGORITHMS["binary"](arr, 7) == 3
    assert SEARCH_ALGORITHMS["binary"](arr, 10) is None
    assert SEARCH_ALGORITHMS["binary"](arr, 1) == 0


def test_jump_search():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert SEARCH_ALGORITHMS["jump"](arr, 11) == 5
    assert SEARCH_ALGORITHMS["jump"](arr, 4) is None


def test_exponential_search():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert SEARCH_ALGORITHMS["exponential"](arr, 1) == 0
    assert SEARCH_ALGORITHMS["exponential"](arr, 15) == 7
    assert SEARCH_ALGORITHMS["exponential"](arr, 6) is None


# ---------- Graph Tests ----------

GRAPH = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def test_bfs():
    result = bfs(GRAPH, "A")
    assert result[0] == "A"
    assert set(result) == {"A", "B", "C", "D", "E", "F"}


def test_dfs():
    result = dfs(GRAPH, "A")
    assert result[0] == "A"
    assert set(result) == {"A", "B", "C", "D", "E", "F"}


def test_dijkstra():
    weighted_graph = {
        "A": {"B": 4, "C": 2},
        "B": {"A": 4, "D": 3, "E": 1},
        "C": {"A": 2, "F": 5},
        "D": {"B": 3},
        "E": {"B": 1, "F": 1},
        "F": {"C": 5, "E": 1},
    }
    distances = dijkstra(weighted_graph, "A")
    assert distances["A"] == 0
    assert distances["B"] == 4
    assert distances["F"] == 7


def test_has_cycle():
    cyclic = {"A": ["B"], "B": ["C"], "C": ["A"]}
    assert has_cycle(cyclic) is True
    acyclic = {"A": ["B"], "B": ["C"], "C": []}
    assert has_cycle(acyclic) is False


if __name__ == "__main__":
    test_sorting_all()
    test_linear_search()
    test_binary_search()
    test_jump_search()
    test_exponential_search()
    test_bfs()
    test_dfs()
    test_dijkstra()
    test_has_cycle()
    print("All tests passed! ✅")
