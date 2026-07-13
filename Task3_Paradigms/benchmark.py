"""
Empirical benchmark for Task 3: Dynamic Programming, Greedy, and
Backtracking. Each algorithm is compared against a brute-force/naive
baseline of worse complexity, at increasing input sizes, to show the
practical payoff of the chosen approach. Writes CSVs + comparison
graphs, matching the methodology used in Task 1 and Task 2.
"""

import time
import random
import csv
import matplotlib.pyplot as plt

from weighted_job_scheduling import weighted_job_scheduling, weighted_job_scheduling_naive
from min_platforms import min_platforms
from hamiltonian_path import hamiltonian_path

RESULTS_DIR = "."


def time_it(fn, *args):
    start = time.perf_counter()
    fn(*args)
    return time.perf_counter() - start


# ---------------- 4.1 Dynamic Programming ----------------
def generate_jobs(n, seed=42):
    random.seed(seed)
    jobs = []
    for _ in range(n):
        start = random.randint(0, 10000)
        end = start + random.randint(1, 200)
        profit = random.randint(1, 1000)
        jobs.append((start, end, profit))
    return jobs


def benchmark_dp():
    sizes = [100, 500, 1000, 2000, 4000]
    rows = []
    for n in sizes:
        jobs = generate_jobs(n)
        opt_t = time_it(weighted_job_scheduling, jobs)
        naive_t = time_it(weighted_job_scheduling_naive, jobs)
        rows.append(["DP", n, opt_t, naive_t])
        print(f"DP n={n:<6} optimised={opt_t:.6f}s naive={naive_t:.6f}s")

    with open("task3_dp_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "optimised_sec", "naive_sec"])
        writer.writerows([[r[1], r[2], r[3]] for r in rows])

    plt.figure(figsize=(7, 5))
    plt.plot(sizes, [r[2] for r in rows], marker="o", label="Optimised O(n log n)")
    plt.plot(sizes, [r[3] for r in rows], marker="o", label="Naive O(n^2)")
    plt.xlabel("Number of jobs (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Weighted Job Scheduling: optimised vs naive DP")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("task3_dp_comparison.png", dpi=150, bbox_inches="tight")
    plt.close()
    return rows


# ---------------- 4.2 Greedy ----------------
def generate_schedule(n, seed=42):
    random.seed(seed)
    arrivals = [random.randint(0, 10000) for _ in range(n)]
    departures = [a + random.randint(1, 100) for a in arrivals]
    return arrivals, departures


def brute_force_platforms(arrivals, departures):
    n = len(arrivals)
    best = 0
    for t in arrivals:
        count = sum(1 for i in range(n) if arrivals[i] <= t <= departures[i])
        best = max(best, count)
    return best


def benchmark_greedy():
    sizes = [100, 500, 1000, 2000]
    rows = []
    for n in sizes:
        arrivals, departures = generate_schedule(n)
        greedy_t = time_it(min_platforms, arrivals, departures)
        brute_t = time_it(brute_force_platforms, arrivals, departures)
        rows.append(["Greedy", n, greedy_t, brute_t])
        print(f"Greedy n={n:<6} greedy={greedy_t:.6f}s brute_force={brute_t:.6f}s")

    with open("task3_greedy_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "greedy_sec", "brute_force_sec"])
        writer.writerows([[r[1], r[2], r[3]] for r in rows])

    plt.figure(figsize=(7, 5))
    plt.plot(sizes, [r[2] for r in rows], marker="o", label="Greedy O(n log n)")
    plt.plot(sizes, [r[3] for r in rows], marker="o", label="Brute force O(n^2)")
    plt.xlabel("Number of trains (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Minimum Platforms: greedy vs brute force")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("task3_greedy_comparison.png", dpi=150, bbox_inches="tight")
    plt.close()
    return rows


# ---------------- 4.3 Backtracking ----------------
def generate_random_graph(n, edge_prob, seed=42):
    random.seed(seed)
    nodes = list(range(n))
    adj = {u: [] for u in nodes}
    for u in nodes:
        for v in nodes:
            if u != v and random.random() < edge_prob:
                adj[u].append(v)
    return adj


def generate_no_path_graph(n):
    """A graph where the last vertex has no edges in either direction,
    guaranteeing no Hamiltonian path exists. The rest of the graph is
    complete, so the search must exhaust every ordering of the other
    n-1 vertices before concluding failure, exposing the O(V!)
    worst-case cost that pruning normally hides."""
    nodes = list(range(n))
    reachable = nodes[:-1]
    adj = {u: [v for v in reachable if v != u] for u in reachable}
    adj[nodes[-1]] = []  # isolated vertex, unreachable and reaches nothing
    return adj


def benchmark_backtracking():
    sizes = [8, 10, 12, 14, 16]
    densities = [("sparse", 0.3), ("dense", 0.6)]
    rows = []
    for label, prob in densities:
        for n in sizes:
            adj = generate_random_graph(n, prob)
            start = time.perf_counter()
            result = hamiltonian_path(adj, 0)
            elapsed = time.perf_counter() - start
            found = result is not None
            rows.append([label, n, elapsed, found])
            print(f"Backtracking {label:<9} n={n:<3} time={elapsed:.6f}s found={found}")

    worst_sizes = [6, 7, 8, 9, 10]
    for n in worst_sizes:
        adj = generate_no_path_graph(n)
        start = time.perf_counter()
        result = hamiltonian_path(adj, 0)
        elapsed = time.perf_counter() - start
        rows.append(["worst_case_no_path", n, elapsed, result is not None])
        print(f"Backtracking worst_case n={n:<3} time={elapsed:.6f}s found={result is not None}")

    with open("task3_backtracking_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["density", "n", "time_sec", "found"])
        writer.writerows(rows)

    plt.figure(figsize=(7, 5))
    for label, _ in densities + [("worst_case_no_path", None)]:
        xs = [r[1] for r in rows if r[0] == label]
        ys = [r[2] for r in rows if r[0] == label]
        plt.plot(xs, ys, marker="o", label=label.replace("_", " "))
    plt.xlabel("Number of vertices (n)")
    plt.ylabel("Time (seconds)")
    plt.yscale("log")
    plt.title("Hamiltonian Path: runtime vs graph density (log scale)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("task3_backtracking_comparison.png", dpi=150, bbox_inches="tight")
    plt.close()
    return rows


if __name__ == "__main__":
    print("=" * 50)
    print("TASK 3 BENCHMARK SUITE")
    print("=" * 50)

    print("\n--- Dynamic Programming ---")
    benchmark_dp()

    print("\n--- Greedy ---")
    benchmark_greedy()

    print("\n--- Backtracking ---")
    benchmark_backtracking()

    print("\nAll results written to task3_*.csv, graphs saved as task3_*.png")