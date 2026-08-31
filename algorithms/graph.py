"""
Algorithm Arena - Graph Algorithms
===================================
Graph traversal and shortest-path algorithms using adjacency lists.
"""

from typing import List, Dict, Set, Optional
from collections import deque
import heapq


def bfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """Breadth-First Search - O(V + E). Returns nodes in BFS order."""
    visited: Set[str] = set()
    queue = deque([start])
    visited.add(start)
    order: List[str] = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dfs(graph: Dict[str, List[str]], start: str) -> List[str]:
    """Depth-First Search - O(V + E). Returns nodes in DFS order (iterative)."""
    visited: Set[str] = set()
    stack = [start]
    order: List[str] = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return order


def dfs_recursive(graph: Dict[str, List[str]], start: str) -> List[str]:
    """Depth-First Search (recursive) - O(V + E)."""
    visited: Set[str] = set()
    order: List[str] = []
    def _dfs(node: str) -> None:
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _dfs(neighbor)
    _dfs(start)
    return order


def dijkstra(graph: Dict[str, Dict[str, float]], start: str) -> Dict[str, float]:
    """Dijkstra's Shortest Path - O((V + E) log V).
    
    Args:
        graph: adjacency dict where graph[node] = {neighbor: weight, ...}
        start: starting node
    
    Returns:
        Dict mapping each node to its shortest distance from start.
    """
    distances: Dict[str, float] = {start: 0}
    pq = [(0, start)]
    visited: Set[str] = set()
    while pq:
        dist, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph.get(node, {}).items():
            new_dist = dist + weight
            if neighbor not in distances or new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distances


def has_cycle(graph: Dict[str, List[str]]) -> bool:
    """Detect if a directed graph has a cycle using DFS.
    Uses 3-color marking: white(undiscovered), gray(in-progress), black(done).
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color: Dict[str, int] = {}
    for node in graph:
        color[node] = WHITE
    def _visit(node: str) -> bool:
        color[node] = GRAY
        for neighbor in graph.get(node, []):
            if color.get(neighbor, WHITE) == GRAY:
                return True
            if color.get(neighbor, WHITE) == WHITE:
                if _visit(neighbor):
                    return True
        color[node] = BLACK
        return False
    for node in graph:
        if color[node] == WHITE:
            if _visit(node):
                return True
    return False
