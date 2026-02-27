"""
Dijkstra's Shortest Path Algorithm
===================================
Finds the shortest path from a source node to all other nodes
in a weighted graph with non-negative edge weights.

Time Complexity: O((V + E) log V) with min-heap
Space Complexity: O(V)
"""

import heapq


def dijkstra(graph, start):
    """
    Run Dijkstra's algorithm on a weighted graph.

    Args:
        graph: dict of {node: [(neighbor, weight), ...]}
        start: source node

    Returns:
        dist: dict of shortest distances from start to each node
        prev: dict of previous node in shortest path
    """
    # Step 1: Initialize distances to infinity, source to 0
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0

    # Min-heap: (distance, node)
    heap = [(0, start)]
    visited = set()

    while heap:
        # Step 2: Extract the unvisited node with minimum distance
        current_dist, u = heapq.heappop(heap)

        # Skip if already visited (stale entry in heap)
        if u in visited:
            continue

        # Step 3: Mark node as visited
        visited.add(u)

        # Step 4: Relax all edges from current node
        for v, weight in graph[u]:
            if v in visited:
                continue

            new_dist = current_dist + weight

            # If we found a shorter path, update
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(heap, (new_dist, v))

    return dist, prev


def reconstruct_path(prev, target):
    """Reconstruct shortest path from source to target."""
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    return list(reversed(path))


# ── Example ──────────────────────────────────────────────────

if __name__ == "__main__":
    # Same graph as the "Empire Network" level (Dijkstra Hard)
    #
    #   A --5-- B --1-- D --3-- F --4-- H
    #   |       |       |               |
    #   2       8       2               3
    #   |       |       |               |
    #   C --4-- E --1-- G ──────────────┘
    #   |
    #   └──6── D  (edge C-D)
    #
    graph = {
        'A': [('B', 5), ('C', 2)],
        'B': [('A', 5), ('D', 1), ('F', 8)],
        'C': [('A', 2), ('E', 4), ('D', 6)],
        'D': [('B', 1), ('C', 6), ('F', 3), ('G', 2)],
        'E': [('C', 4), ('G', 1)],
        'F': [('B', 8), ('D', 3), ('H', 4)],
        'G': [('D', 2), ('E', 1), ('H', 3)],
        'H': [('F', 4), ('G', 3)],
    }

    print("=== Dijkstra's Algorithm ===\n")
    print("Graph (adjacency list):")
    for node, edges in sorted(graph.items()):
        edges_str = ", ".join(f"{v}({w})" for v, w in edges)
        print(f"  {node}: {edges_str}")

    dist, prev = dijkstra(graph, 'A')

    print(f"\nShortest paths from A to every node:")
    print(f"  {'To':<6} {'Dist':<6} {'Full path from A'}")
    print(f"  {'─'*6} {'─'*6} {'─'*25}")
    for node in sorted(dist):
        path = reconstruct_path(prev, node)
        path_str = " → ".join(path)
        print(f"  {node:<6} {dist[node]:<6} {path_str}")
