"""
Bellman-Ford algorithm - single-source shortest path, handles negative
weights and detects negative cycles. O(V * E).
"""

from graph import Graph


def bellman_ford(graph, source):
    dist = {node: float("inf") for node in graph.nodes()}
    prev = {node: None for node in graph.nodes()}
    dist[source] = 0
    edges = graph.edges()

    # Relax all edges |V|-1 times
    for _ in range(graph.num_nodes() - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                updated = True
        if not updated:
            break  # early exit once no edge relaxes further

    # One more pass to detect negative cycles
    negative_cycle = False
    for u, v, w in edges:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            negative_cycle = True
            break

    return dist, prev, negative_cycle


if __name__ == "__main__":
    g = Graph(directed=True)
    g.add_edge("Kathmandu", "Pokhara", 200)
    g.add_edge("Kathmandu", "Butwal", 280)
    g.add_edge("Pokhara", "Butwal", -50)  # negative weight edge
    g.add_edge("Butwal", "Biratnagar", 350)

    print("=" * 50)
    print("BELLMAN-FORD ALGORITHM - DEMO")
    print("=" * 50)

    print("\nShortest Paths from Kathmandu (with negative edge):")
    dist, prev, has_neg_cycle = bellman_ford(g, "Kathmandu")
    for node in g.nodes():
        print(f"  {node:<12} -> distance={dist[node]}")

    print(f"\nNegative Cycle Detected: {has_neg_cycle}")

    print("\nNegative Cycle Test:")
    g2 = Graph(directed=True)
    g2.add_edge("A", "B", 1)
    g2.add_edge("B", "C", -3)
    g2.add_edge("C", "A", 1)  # A->B->C->A = -1, negative cycle
    _, _, has_neg_cycle2 = bellman_ford(g2, "A")
    print(f"  Cycle A->B->C->A -> Negative Cycle Detected: {has_neg_cycle2}")
