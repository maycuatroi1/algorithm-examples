"""
Prim-Jarník's Minimum Spanning Tree Algorithm
===============================================
Builds a minimum spanning tree by greedily adding the cheapest
edge that connects a new vertex to the growing tree.

Time Complexity: O((V + E) log V) with min-heap
Space Complexity: O(V)
"""

import heapq


def prim(graph, start):
    """
    Run Prim's algorithm to find the Minimum Spanning Tree.

    Args:
        graph: dict of {node: [(neighbor, weight), ...]}
        start: starting node

    Returns:
        mst_edges: list of (from, to, weight) edges in the MST
        total_weight: total weight of the MST
    """
    # Step 1: Initialize
    in_mst = set()
    mst_edges = []
    # Min-heap: (weight, current_node, parent_node)
    heap = [(0, start, None)]

    while heap and len(in_mst) < len(graph):
        # Step 2: Extract minimum-weight edge connecting to a new node
        weight, u, parent = heapq.heappop(heap)

        # Skip if already in MST
        if u in in_mst:
            continue

        # Step 3: Add node to MST
        in_mst.add(u)

        if parent is not None:
            mst_edges.append((parent, u, weight))

        # Step 4: Add all edges from new node to the heap
        for v, w in graph[u]:
            if v not in in_mst:
                heapq.heappush(heap, (w, v, u))

    total_weight = sum(w for _, _, w in mst_edges)
    return mst_edges, total_weight


# ── Example ──────────────────────────────────────────────────

if __name__ == "__main__":
    # Same graph as the "Ancient Aqueducts" level (Prim Hard)
    #
    #   A --4-- B --2-- D --6-- F --2-- H
    #   |       |       |       |       |
    #   8       5       1       7       3
    #   |       |       |       |       |
    #   C ──────┘       E --4-- G ──────┘
    #   |                       |
    #   └───────3───────E───────┘
    #
    graph = {
        'A': [('B', 4), ('C', 8)],
        'B': [('A', 4), ('D', 2), ('C', 5)],
        'C': [('A', 8), ('B', 5), ('E', 3)],
        'D': [('B', 2), ('F', 6), ('E', 1), ('G', 7)],
        'E': [('C', 3), ('D', 1), ('G', 4)],
        'F': [('D', 6), ('H', 2)],
        'G': [('D', 7), ('E', 4), ('H', 3)],
        'H': [('F', 2), ('G', 3)],
    }

    print("=== Prim-Jarník's MST Algorithm ===\n")
    print("Graph (adjacency list):")
    for node, edges in sorted(graph.items()):
        edges_str = ", ".join(f"{v}({w})" for v, w in edges)
        print(f"  {node}: {edges_str}")

    mst_edges, total_weight = prim(graph, 'A')

    print(f"\nMinimum Spanning Tree edges:")
    print(f"  {'From':<6} {'To':<6} {'Weight'}")
    print(f"  {'─'*6} {'─'*6} {'─'*6}")
    for u, v, w in mst_edges:
        print(f"  {u:<6} {v:<6} {w}")

    print(f"\nTotal MST weight: {total_weight}")
    print(f"MST has {len(mst_edges)} edges for {len(graph)} nodes")
