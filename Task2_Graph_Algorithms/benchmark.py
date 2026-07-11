"""
Empirical benchmark: Dijkstra vs Prim vs Bellman-Ford on sparse and
dense random graphs of increasing size. Measures wall-clock time and
writes results to CSV + comparison graphs.
"""

import time
import random
import csv
import matplotlib.pyplot as plt

from graph import Graph
from dijkstra import dijkstra
from prim import prim
from bellman_ford import bellman_ford

SIZES = [50, 100, 200]
RESULTS_CSV = "benchmark_results.csv"


def make_sparse_graph(n, seed=42):
    """Roughly 2n edges: a random spanning tree plus a few extra edges."""
    random.seed(seed)
    g = Graph(directed=True)
    nodes = list(range(n))
    for node in nodes:
        g.add_node(node)
    # random spanning tree ensures connectivity
    for i in range(1, n):
        parent = random.randint(0, i - 1)
        g.add_edge(parent, i, random.randint(1, 100))
    # a few extra random edges (total ~2n)
    for _ in range(n):
        u, v = random.sample(nodes, 2)
        g.add_edge(u, v, random.randint(1, 100))
    return g


def make_dense_graph(n, seed=42):
    """Roughly n^2/4 edges."""
    random.seed(seed)
    g = Graph(directed=True)
    nodes = list(range(n))
    for node in nodes:
        g.add_node(node)
    for i in range(1, n):
        parent = random.randint(0, i - 1)
        g.add_edge(parent, i, random.randint(1, 100))
    target_edges = (n * n) // 4
    while g.num_edges() < target_edges:
        u, v = random.sample(nodes, 2)
        g.add_edge(u, v, random.randint(1, 100))
    return g


def time_it(fn, *args):
    start = time.perf_counter()
    fn(*args)
    return time.perf_counter() - start


def run_benchmarks():
    rows = []
    for n in SIZES:
        for density, builder in [("sparse", make_sparse_graph), ("dense", make_dense_graph)]:
            g = builder(n)
            e = g.num_edges()
            undirected = g.to_undirected()

            dijkstra_t = time_it(dijkstra, g, 0)
            prim_t = time_it(prim, undirected)
            bf_t = time_it(bellman_ford, g, 0)

            rows.append([density, n, e, dijkstra_t, prim_t, bf_t])
            print(f"{density:<7} n={n:<5} e={e:<6} done")

    with open(RESULTS_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["density", "n", "edges", "dijkstra_sec", "prim_sec", "bellman_ford_sec"])
        writer.writerows(rows)

    return rows


def plot_results(rows):
    algorithms = [("dijkstra_sec", 3, "Dijkstra"), ("prim_sec", 4, "Prim"), ("bellman_ford_sec", 5, "Bellman-Ford")]

    for density in ["sparse", "dense"]:
        plt.figure(figsize=(7, 5))
        for col_name, col_idx, label in algorithms:
            xs = [r[1] for r in rows if r[0] == density]
            ys = [r[col_idx] for r in rows if r[0] == density]
            plt.plot(xs, ys, marker="o", label=label)
        plt.xlabel("Number of nodes (n)")
        plt.ylabel("Time (seconds)")
        plt.title(f"Algorithm runtime vs n ({density} graph)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        fname = f"task2_{density}_comparison.png"
        plt.savefig(fname, dpi=150, bbox_inches="tight")
        plt.close()
        print(f"Saved {fname}")


if __name__ == "__main__":
    results = run_benchmarks()
    plot_results(results)
    print(f"\nResults written to {RESULTS_CSV}")
