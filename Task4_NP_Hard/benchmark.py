"""
Empirical comparison of the two VRPTW heuristics across increasing
customer counts: solution quality (total distance) and runtime.
"""

import time
import csv
import matplotlib.pyplot as plt

from vrptw import generate_instance, total_distance
from greedy_heuristic import greedy_construct
from local_search import local_search

SIZES = [10, 20, 30, 50, 75, 100]
RESULTS_CSV = "task4_results.csv"


def time_it(fn, *args):
    start = time.perf_counter()
    result = fn(*args)
    return result, time.perf_counter() - start


def run_benchmarks():
    rows = []
    for n in SIZES:
        customers, capacity = generate_instance(n_customers=n)

        greedy_routes, greedy_t = time_it(greedy_construct, customers, capacity)
        greedy_dist = total_distance(greedy_routes, customers)

        improved_routes, ls_t = time_it(local_search, greedy_routes, customers, capacity)
        improved_dist = total_distance(improved_routes, customers)
        total_ls_t = greedy_t + ls_t  # greedy + 2-opt combined runtime

        improvement_pct = (1 - improved_dist / greedy_dist) * 100

        rows.append([n, greedy_dist, greedy_t, improved_dist, total_ls_t, improvement_pct])
        print(f"n={n:<4} greedy_dist={greedy_dist:8.2f} ({greedy_t:.4f}s)  "
              f"2opt_dist={improved_dist:8.2f} ({total_ls_t:.4f}s)  "
              f"improvement={improvement_pct:.1f}%")

    with open(RESULTS_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "greedy_distance", "greedy_sec",
                          "2opt_distance", "2opt_sec", "improvement_pct"])
        writer.writerows(rows)

    return rows


def plot_results(rows):
    sizes = [r[0] for r in rows]

    plt.figure(figsize=(7, 5))
    plt.plot(sizes, [r[1] for r in rows], marker="o", label="Greedy only")
    plt.plot(sizes, [r[3] for r in rows], marker="o", label="Greedy + 2-opt")
    plt.xlabel("Number of customers (n)")
    plt.ylabel("Total route distance")
    plt.title("VRPTW: solution quality vs problem size")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("task4_quality_comparison.png", dpi=150, bbox_inches="tight")
    plt.close()

    plt.figure(figsize=(7, 5))
    plt.plot(sizes, [r[2] for r in rows], marker="o", label="Greedy only")
    plt.plot(sizes, [r[4] for r in rows], marker="o", label="Greedy + 2-opt")
    plt.xlabel("Number of customers (n)")
    plt.ylabel("Time (seconds)")
    plt.title("VRPTW: runtime vs problem size")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("task4_runtime_comparison.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("\nSaved task4_quality_comparison.png and task4_runtime_comparison.png")


if __name__ == "__main__":
    results = run_benchmarks()
    plot_results(results)
    print(f"\nResults written to {RESULTS_CSV}")