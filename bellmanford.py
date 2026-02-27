"""
Bellman-Ford Shortest Path Algorithm
=====================================
Finds the shortest path from a source node to all other nodes
in a weighted graph. Unlike Dijkstra, supports negative edge weights.

Time Complexity: O(V * E)
Space Complexity: O(V)
"""


def bellman_ford(graph, edges, start):
    """
    Run Bellman-Ford algorithm on a weighted graph.

    Args:
        graph: dict of {node: [(neighbor, weight), ...]}
        edges: list of (u, v, weight) tuples
        start: source node

    Returns:
        dist: dict of shortest distances from start to each node
        prev: dict of previous node in shortest path
        has_negative_cycle: True if a negative-weight cycle is reachable
    """
    # Step 1: Initialize distances to infinity, source to 0
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[start] = 0

    V = len(graph)

    # Step 2: Relax all edges V-1 times
    for i in range(V - 1):
        for u, v, weight in edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                prev[v] = u

    # Step 3: Check for negative-weight cycles
    has_negative_cycle = False
    for u, v, weight in edges:
        if dist[u] != float('inf') and dist[u] + weight < dist[v]:
            has_negative_cycle = True
            break

    return dist, prev, has_negative_cycle


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
    # Same graph as the "Negative Currents" level (Bellman-Ford Medium)
    #
    #   A --4-- B ---(-1)--- C
    #   |       |            |
    #   2       3            5
    #   |       |            |
    #   C       D ---(-2)--- E --3-- F
    #           |                    |
    #           └──────2─────────────┘
    #
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', -1), ('D', 3)],
        'C': [('A', 2), ('B', -1), ('E', 5)],
        'D': [('B', 3), ('E', -2), ('F', 2)],
        'E': [('C', 5), ('D', -2), ('F', 3)],
        'F': [('D', 2), ('E', 3)],
    }

    # Build directed edge list (both directions for undirected graph)
    edges = []
    for u, neighbors in graph.items():
        for v, w in neighbors:
            edges.append((u, v, w))

    print("=== Bellman-Ford Algorithm ===\n")
    print("Graph (adjacency list):")
    for node, neighbors in sorted(graph.items()):
        edges_str = ", ".join(f"{v}({w})" for v, w in neighbors)
        print(f"  {node}: {edges_str}")

    dist, prev, has_neg_cycle = bellman_ford(graph, edges, 'A')

    if has_neg_cycle:
        print("\nWARNING: Negative-weight cycle detected!")
    else:
        print(f"\nShortest paths from A to every node:")
        print(f"  {'To':<6} {'Dist':<6} {'Full path from A'}")
        print(f"  {'─'*6} {'─'*6} {'─'*25}")
        for node in sorted(dist):
            path = reconstruct_path(prev, node)
            path_str = " → ".join(path)
            print(f"  {node:<6} {dist[node]:<6} {path_str}")
