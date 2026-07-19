"""
Empirical benchmark: sequential merge sort vs parallel merge sort at
1, 2, 4, and 8 workers. Measures wall-clock time and speedup
(sequential_time / parallel_time) to analyse scalability.
"""

import time
import csv
import matplotlib.pyplot as plt

from sequential_sort import merge_sort, generate_cities
from parallel_sort import parallel_merge_sort

N_CITIES = 200_000
WORKER_COUNTS = [1, 2, 4, 8]
RESULTS_CSV = "task5_results.csv"


def time_it(fn, *args, **kwargs):
    start = time.perf_counter()
    fn(*args, **kwargs)
    return time.perf_counter() - start


def run_benchmarks():
    cities = generate_cities(N_CITIES)

    print(f"Sorting {N_CITIES} cities\n")

    seq_t = time_it(merge_sort, cities)
    print(f"Sequential (1 thread, no pool): {seq_t:.4f}s")

    rows = [[1, seq_t, 1.0]]

    for workers in WORKER_COUNTS:
        if workers == 1:
            continue
        par_t = time_it(parallel_merge_sort, cities, workers)
        speedup = seq_t / par_t
        rows.append([workers, par_t, speedup])
        print(f"Parallel ({workers} workers): {par_t:.4f}s  speedup={speedup:.2f}x")

    with open(RESULTS_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["workers", "time_sec", "speedup"])
        writer.writerows(rows)

    return rows


def plot_results(rows):
    workers = [r[0] for r in rows]
    speedup = [r[2] for r in rows]

    plt.figure(figsize=(7, 5))
    plt.plot(workers, speedup, marker="o", label="Measured speedup")
    plt.plot(workers, workers, linestyle="--", color="gray", label="Ideal linear speedup")
    plt.xlabel("Number of workers")
    plt.ylabel("Speedup (sequential time / parallel time)")
    plt.title("Parallel Merge Sort: speedup vs worker count")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("task5_speedup.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("\nSaved task5_speedup.png")


if __name__ == "__main__":
    results = run_benchmarks()
    plot_results(results)
    print(f"\nResults written to {RESULTS_CSV}")