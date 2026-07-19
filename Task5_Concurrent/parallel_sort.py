"""
Parallel merge sort.

Python's threading module cannot give real CPU parallelism for a
CPU-bound sort, since the Global Interpreter Lock (GIL) allows only
one thread to execute Python bytecode at a time. To get genuine
multi-core speedup, this uses multiprocessing instead, which runs
each worker as a separate OS process (an "equivalent threading
library" in the sense the brief allows, since each process is
scheduled independently across cores, exactly like pthreads are).

Strategy: split the city list into P equal chunks (P = worker
count), sort each chunk independently in its own process using the
sequential merge_sort, then merge the P sorted chunks back together
in the main process with a k-way merge.

Synchronisation: workers do not share the array being sorted, so
there is no race there. But a shared progress counter,
"chunks_completed", is incremented by every worker as it finishes,
protected by a multiprocessing.Lock. This models a realistic
scenario (e.g. a shared progress dashboard) where multiple workers
must update common state safely, and is the critical section
analysed in the report.
"""

import heapq
from multiprocessing import Pool, Manager, Lock
from sequential_sort import merge_sort, generate_cities, City


def _sort_chunk(args):
    chunk, counter, lock = args
    sorted_chunk = merge_sort(chunk)
    with lock:  # critical section: safely increment shared counter
        counter.value += 1
    return sorted_chunk


def k_way_merge(sorted_chunks):
    """Merge P already-sorted chunks into one sorted list. O(n log P)."""
    heap = []
    for i, chunk in enumerate(sorted_chunks):
        if chunk:
            heapq.heappush(heap, (chunk[0].distance, i, 0))

    result = []
    while heap:
        dist, chunk_idx, elem_idx = heapq.heappop(heap)
        result.append(sorted_chunks[chunk_idx][elem_idx])
        next_idx = elem_idx + 1
        if next_idx < len(sorted_chunks[chunk_idx]):
            nxt = sorted_chunks[chunk_idx][next_idx]
            heapq.heappush(heap, (nxt.distance, chunk_idx, next_idx))

    return result


def parallel_merge_sort(cities, num_workers):
    if num_workers <= 1:
        return merge_sort(cities), 0  # sequential fallback

    manager = Manager()
    counter = manager.Value("i", 0)
    lock = manager.Lock()

    chunk_size = (len(cities) + num_workers - 1) // num_workers
    chunks = [cities[i:i + chunk_size] for i in range(0, len(cities), chunk_size)]

    with Pool(processes=num_workers) as pool:
        sorted_chunks = pool.map(_sort_chunk, [(c, counter, lock) for c in chunks])

    result = k_way_merge(sorted_chunks)
    return result, counter.value


if __name__ == "__main__":
    cities = generate_cities(20)

    print("=" * 50)
    print("PARALLEL MERGE SORT - DEMO")
    print("=" * 50)

    print(f"\nWorkers: 4")
    sorted_cities, chunks_completed = parallel_merge_sort(cities, num_workers=4)

    print("\nAfter Sorting (first 5, by distance):")
    for c in sorted_cities[:5]:
        print(f"  {c}")

    is_sorted = all(sorted_cities[i].distance <= sorted_cities[i + 1].distance
                     for i in range(len(sorted_cities) - 1))
    print(f"\nSorted Correctly: {is_sorted}")
    print(f"Chunks Completed (via locked counter): {chunks_completed}")