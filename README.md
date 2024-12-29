# DIJKSTRA
Dijkstra's algorithm is one of the finding paths algorithms.
# Dijkstra's Algorithm Implementation

This repository contains a simple implementation of Dijkstra's algorithm in Python. The algorithm is used to find the shortest paths from a source node to all other nodes in a weighted graph.

## Code Overview

### Function: `dijkstra(graph, source)`
This function calculates the shortest distances from the `source` node to all other nodes in the graph using Dijkstra's algorithm.

#### Parameters:
- `graph`: A dictionary representing the graph, where each key is a node and its value is another dictionary containing neighboring nodes as keys and their weights as values.
- `source`: The starting node for the algorithm.

#### Returns:
- A dictionary containing the shortest distances from the source node to each node in the graph.

### Example Input
```python
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 2},
    'C': {'A': 10, 'B': 3, 'D': 4},
    'D': {'B': 2, 'C': 4}
}

source_node = "A"
