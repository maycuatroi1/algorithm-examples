"""
Kruskal's Minimum Spanning Tree Algorithm
==========================================
Builds a minimum spanning tree by sorting all edges by weight
and greedily adding edges that don't create a cycle.

Uses Union-Find (Disjoint Set) for efficient cycle detection.

Time Complexity: O(E log E) for sorting edges
Space Complexity: O(V) for Union-Find
"""


class UnionFind:
    """
    Disjoint Set Union with path compression and union by rank.
    Used to efficiently detect cycles when adding edges.
    """

    def __init__(self, elements):
        self.parent = {x: x for x in elements}
        self.rank = {x: 0 for x in elements}

    def find(self, x):
        """Find root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        """
        Union two sets by rank.
        Returns True if x and y were in different sets (merged).
        Returns False if they were already connected (cycle!).
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Same set → would create a cycle

        # Union by rank: attach smaller tree under larger tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

    def connected(self, x, y):
        """Check if x and y are in the same set."""
        return self.find(x) == self.find(y)


def kruskal(nodes, edges):
    """
    Run Kruskal's algorithm to find the Minimum Spanning Tree.

    Args:
        nodes: list of node identifiers
        edges: list of (from, to, weight) tuples

    Returns:
        mst_edges: list of (from, to, weight) edges in the MST
        total_weight: total weight of the MST
    """
    # Step 1: Sort all edges by weight (ascending)
    sorted_edges = sorted(edges, key=lambda e: e[2])

    # Step 2: Initialize Union-Find
    uf = UnionFind(nodes)
    mst_edges = []

    # Step 3: Process edges in order of weight
    for u, v, weight in sorted_edges:
        # Step 4: Check if adding this edge creates a cycle
        if uf.connected(u, v):
            # REJECT: u and v are already connected → cycle
            continue

        # Step 5: ACCEPT: add edge to MST and union the sets
        uf.union(u, v)
        mst_edges.append((u, v, weight))

        # MST is complete when we have V-1 edges
        if len(mst_edges) == len(nodes) - 1:
            break

    total_weight = sum(w for _, _, w in mst_edges)
    return mst_edges, total_weight


# ── Example ──────────────────────────────────────────────────

if __name__ == "__main__":
    # Same graph as the "Dragon Mail" level (Kruskal Hard)
    #
    #   A --3-- B --1-- D --5-- F --1-- H
    #   |       |       |       |       |
    #   6       7       4       8       2
    #   |       |       |       |       |
    #   C ──────┘       E --3-- G ──────┘
    #   |                       |
    #   └───────2───────E───────┘
    #
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    edges = [
        ('A', 'B', 3),
        ('A', 'C', 6),
        ('B', 'D', 1),
        ('B', 'C', 7),
        ('C', 'E', 2),
        ('D', 'F', 5),
        ('D', 'E', 4),
        ('D', 'G', 8),
        ('E', 'G', 3),
        ('F', 'H', 1),
        ('G', 'H', 2),
    ]

    print("=== Kruskal's MST Algorithm ===\n")

    print("All edges (sorted by weight):")
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        print(f"  {u}-{v}: weight {w}")

    mst_edges, total_weight = kruskal(nodes, edges)

    print(f"\nMinimum Spanning Tree edges:")
    print(f"  {'From':<6} {'To':<6} {'Weight':<8} {'Action'}")
    print(f"  {'─'*6} {'─'*6} {'─'*8} {'─'*10}")

    # Show the full process
    uf = UnionFind(nodes)
    sorted_edges = sorted(edges, key=lambda e: e[2])
    for u, v, w in sorted_edges:
        if uf.connected(u, v):
            print(f"  {u:<6} {v:<6} {w:<8} REJECT (cycle)")
        else:
            uf.union(u, v)
            print(f"  {u:<6} {v:<6} {w:<8} ACCEPT ✓")

    print(f"\nTotal MST weight: {total_weight}")
    print(f"MST has {len(mst_edges)} edges for {len(nodes)} nodes")
