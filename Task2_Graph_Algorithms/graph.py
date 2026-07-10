"""
Weighted directed graph for a city transportation network.
Adjacency-list representation: for a sparse road network (edges << n^2),
this gives O(V+E) space instead of adjacency matrix's O(V^2), and
O(deg(v)) neighbour iteration instead of O(V) per row scan.
"""


class Graph:
    def __init__(self, directed=True):
        self.directed = directed
        self.adj = {}  # node -> list of (neighbour, weight)

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u, v, weight):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def nodes(self):
        return list(self.adj.keys())

    def edges(self):
        result = []
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u]:
                if self.directed or (v, u) not in seen:
                    result.append((u, v, w))
                    seen.add((u, v))
        return result

    def neighbours(self, u):
        return self.adj[u]

    def num_nodes(self):
        return len(self.adj)

    def num_edges(self):
        return len(self.edges())

    def to_undirected(self):
        """Return an undirected copy (needed for MST construction)."""
        g = Graph(directed=False)
        seen = set()
        for u in self.adj:
            for v, w in self.adj[u]:
                key = tuple(sorted((u, v)))
                if key not in seen:
                    g.add_edge(u, v, w)
                    seen.add(key)
        return g


if __name__ == "__main__":
    g = Graph(directed=True)
    g.add_edge("Kathmandu", "Pokhara", 200)
    g.add_edge("Kathmandu", "Butwal", 280)
    g.add_edge("Pokhara", "Butwal", 120)

    print("=" * 50)
    print("GRAPH - DEMO")
    print("=" * 50)
    print(f"\nNodes: {g.num_nodes()}")
    print(f"Edges: {g.num_edges()}")
    print("\nAdjacency List:")
    for u in g.nodes():
        for v, w in g.neighbours(u):
            print(f"  {u} -> {v} (w={w})")
