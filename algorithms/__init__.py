"""Algorithm Arena - A collection of classic algorithm implementations."""

from .sorting import ALGORITHMS as SORTING_ALGORITHMS
from .searching import SEARCH_ALGORITHMS
from .graph import bfs, dfs, dfs_recursive, dijkstra, has_cycle

__version__ = "1.0.0"
__author__ = "Samrat Barman"

__all__ = [
    "SORTING_ALGORITHMS",
    "SEARCH_ALGORITHMS",
    "bfs",
    "dfs",
    "dfs_recursive",
    "dijkstra",
    "has_cycle",
]
