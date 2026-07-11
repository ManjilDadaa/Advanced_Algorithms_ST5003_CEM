"""
Prim's algorithm - Minimum Spanning Tree, undirected graph.
Uses a binary min-heap: O((V + E) log V).
MST is constructed over the undirected version of the transport
network (an MST is only defined for undirected graphs).
"""

import heapq
from graph import Graph


def prim(graph, source=None):
    nodes = graph.nodes()
    if not nodes:
        return [], 0
    source = source or nodes[0]

    visited = {source}
    mst_edges = []
    total_weight = 0
    pq = [(w, source, v) for v, w in graph.neighbours(source)]
    heapq.heapify(pq)

    while pq and len(visited) < len(nodes):
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue
        visited.add(v)
        mst_edges.append((u, v, w))
        total_weight += w
        for nxt, nw in graph.neighbours(v):
            if nxt not in visited:
                heapq.heappush(pq, (nw, v, nxt))

    return mst_edges, total_weight


if __name__ == "__main__":
    g = Graph(directed=True)
    g.add_edge("Kathmandu", "Pokhara", 200)
    g.add_edge("Kathmandu", "Butwal", 280)
    g.add_edge("Pokhara", "Butwal", 120)
    g.add_edge("Pokhara", "Biratnagar", 400)
    g.add_edge("Butwal", "Biratnagar", 350)

    undirected = g.to_undirected()

    print("=" * 50)
    print("PRIM'S ALGORITHM - DEMO")
    print("=" * 50)

    print("\nMST Construction (step by step):")
    mst_edges, total_weight = prim(undirected)
    for u, v, w in mst_edges:
        print(f"  Added edge {u} -- {v} (w={w})")

    print(f"\nTotal MST Weight: {total_weight}")
