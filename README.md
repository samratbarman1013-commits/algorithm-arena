# Algorithm Arena

A collection of classic algorithms implemented in **Python** with a companion **Node.js** benchmarking CLI tool.

## What's Inside

### Python Algorithms (`algorithms/`)

**Sorting** (`sorting.py`)
| Algorithm | Time (avg) | Space | Stable |
|-----------|-----------|-------|--------|
| Bubble Sort | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(1) | No |
| Insertion Sort | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(log n) | No |
| Heap Sort | O(n log n) | O(1) | No |

**Searching** (`searching.py`)
| Algorithm | Time | Requires Sorted |
|-----------|------|-----------------|
| Linear Search | O(n) | No |
| Binary Search | O(log n) | Yes |
| Binary Search (recursive) | O(log n) | Yes |
| Jump Search | O(√n) | Yes |
| Exponential Search | O(log n) | Yes |

**Graph** (`graph.py`)
| Algorithm | Time | Description |
|-----------|------|-------------|
| BFS | O(V + E) | Breadth-first traversal |
| DFS | O(V + E) | Depth-first traversal (iterative) |
| DFS (recursive) | O(V + E) | Depth-first traversal (recursive) |
| Dijkstra | O((V+E) log V) | Shortest path in weighted graph |
| Cycle Detection | O(V + E) | 3-color DFS for directed graphs |

### JavaScript Benchmark CLI (`benchmark/`)

A Node.js CLI tool to benchmark sorting algorithm performance with randomly generated datasets.

```bash
# Run all benchmarks
node benchmark/cli.js

# Custom dataset size
node benchmark/cli.js --size 5000

# Run specific algorithm
node benchmark/cli.js --algo quick

# Output as JSON
node benchmark/cli.js --json
```

## Quick Start

### Python

```python
from algorithms.sorting import ALGORITHMS
from algorithms.searching import SEARCH_ALGORITHMS
from algorithms.graph import bfs, dfs, dijkstra

# Sort with any algorithm
sorted_arr = ALGORITHMS["quick"]([3, 1, 4, 1, 5, 9, 2, 6])

# Search (binary requires sorted input)
idx = SEARCH_ALGORITHMS["binary"]([1, 3, 5, 7, 9], 7)

# Graph traversal
graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A"], "D": ["B"]}
order = bfs(graph, "A")
```

### Run Tests

```bash
python -m pytest tests/ -v
# or simply:
python tests/test_algorithms.py
```

### JavaScript Benchmark

```bash
node benchmark/cli.js --size 5000
```

## Project Structure

```
algorithm-arena/
├── algorithms/
│   ├── __init__.py       # Package exports
│   ├── sorting.py        # 6 sorting algorithms
│   ├── searching.py      # 5 searching algorithms
│   └── graph.py          # BFS, DFS, Dijkstra, cycle detection
├── benchmark/
│   ├── cli.js             # Benchmark CLI tool
│   ├── runner.js          # JS sorting implementations + runner
│   └── package.json       # Node.js config
├── tests/
│   └── test_algorithms.py # Comprehensive test suite
├── README.md
└── LICENSE
```

## Features

- Clean, documented, production-quality code
- All sorting functions return a new list (no mutation of input)
- Comprehensive test suite with edge cases (empty arrays, single elements, sorted/reverse-sorted)
- Cross-language: Python algorithms + JavaScript benchmarking
- MIT License — free to use and learn from

## Author

**Samrat Barman** — Full Stack Developer passionate about Open Source & C++

## License

MIT License — see [LICENSE](LICENSE) for details.
