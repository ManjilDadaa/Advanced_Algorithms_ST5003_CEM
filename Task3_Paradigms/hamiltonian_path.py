"""
Hamiltonian Path / Cycle via backtracking.
Finds a path that visits every vertex of a graph exactly once
(a cycle additionally requires an edge back to the start).
Pruning: only extend to unvisited vertices with a valid edge.
Worst case O(V!), heavily reduced in practice by pruning.
"""


def hamiltonian_path(adj, start, find_cycle=False):
    nodes = list(adj.keys())
    n = len(nodes)
    path = [start]
    visited = {start}

    def backtrack():
        if len(path) == n:
            if not find_cycle:
                return True
            return start in adj[path[-1]]  # edge back to start closes the cycle

        for neighbour in adj[path[-1]]:
            if neighbour not in visited:  # pruning: skip visited vertices
                visited.add(neighbour)
                path.append(neighbour)
                if backtrack():
                    return True
                # backtrack: undo the choice
                path.pop()
                visited.remove(neighbour)
        return False

    found = backtrack()
    return (path if found else None)


if __name__ == "__main__":
    # City network (subset of Task 2's graph, undirected for path purposes)
    adj = {
        "Kathmandu": ["Pokhara", "Butwal"],
        "Pokhara": ["Kathmandu", "Butwal", "Biratnagar"],
        "Butwal": ["Kathmandu", "Pokhara", "Biratnagar"],
        "Biratnagar": ["Pokhara", "Butwal"],
    }

    print("=" * 50)
    print("HAMILTONIAN PATH - DEMO")
    print("=" * 50)

    print("\nGraph (adjacency list):")
    for u, neighbours in adj.items():
        print(f"  {u} -> {neighbours}")

    print("\nSearch (Hamiltonian Path from Kathmandu):")
    result = hamiltonian_path(adj, "Kathmandu")
    if result:
        print(f"  Found -> {' -> '.join(result)}")
    else:
        print("  No Hamiltonian path exists")

    print("\nSearch (Hamiltonian Cycle from Kathmandu):")
    result_cycle = hamiltonian_path(adj, "Kathmandu", find_cycle=True)
    if result_cycle:
        print(f"  Found -> {' -> '.join(result_cycle)} -> Kathmandu")
    else:
        print("  No Hamiltonian cycle exists")