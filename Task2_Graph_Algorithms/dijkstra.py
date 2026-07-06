"""
Dijkstra's algorithm - single-source shortest path, non-negative weights.
Uses a binary min-heap: O((V + E) log V).
"""

import heapq
from graph import Graph


def dijkstra(graph, source):
    dist = {node: float("inf") for node in graph.nodes()}
    prev = {node: None for node in graph.nodes()}
    dist[source] = 0
    visited = set()
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v, w in graph.neighbours(u):
            if w < 0:
                raise ValueError("Dijkstra requires non-negative weights")
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, prev


def reconstruct_path(prev, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    return list(reversed(path))


if __name__ == "__main__":
    g = Graph(directed=True)
    g.add_edge("Kathmandu", "Pokhara", 200)
    g.add_edge("Kathmandu", "Butwal", 280)
    g.add_edge("Pokhara", "Butwal", 120)
    g.add_edge("Pokhara", "Biratnagar", 400)
    g.add_edge("Butwal", "Biratnagar", 350)

    print("=" * 50)
    print("DIJKSTRA'S ALGORITHM - DEMO")
    print("=" * 50)

    print("\nShortest Paths from Kathmandu:")
    dist, prev = dijkstra(g, "Kathmandu")
    for node in g.nodes():
        print(f"  {node:<12} -> distance={dist[node]}")

    print("\nPath Reconstruction:")
    for target in ["Butwal", "Biratnagar"]:
        path = reconstruct_path(prev, target)
        print(f"  To {target:<12}: {' -> '.join(path)} (cost={dist[target]})")
