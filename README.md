# ST5003CEM — Advanced Algorithms

**Student:** Manjil Basnet
**Student ID:** 240623
**Module:** ST5003CEM — Advanced Algorithms
**College:** Softwarica College of IT & E-Commerce
**Language:** Python

---

## Overview

This repository contains the coursework for the ST5003CEM Advanced Algorithms module. The assignment is divided into five tasks unified around a single case study, a city transportation network, covering data structures, graph algorithms, algorithmic paradigms, NP-Hard heuristics, and concurrent programming.

| Task | Topic | Status |
|------|-------|--------|
| Task 1 | Advanced Data Structures | ✅ Completed |
| Task 2 | Graph Algorithms and Pathfinding | ✅ Completed |
| Task 3 | Algorithmic Strategies for Complex Problems | ✅ Completed |
| Task 4 | NP-Hard Problem and Heuristics | ✅ Completed |
| Task 5 | Concurrent Programming | ✅ Completed |

---

## Repository Structure

```
.
├── task1/          # BST, AVL Tree, Min-Heap, Hash Table
├── task2/          # Dijkstra, Prim, Bellman-Ford
├── task3/          # Dynamic Programming, Greedy, Backtracking
├── task4/          # VRPTW heuristics (Greedy, 2-opt local search)
├── task5/          # Parallel merge sort (multiprocessing)
├── report/         # Report source and appendix material
└── README.md
```

---

## Build Requirements

- Python 3.10 or above
- `matplotlib` for benchmark graphs (`pip install matplotlib`)
- No external dependencies beyond the standard library otherwise

---

## Tasks

### Task 1 — Advanced Data Structures

> Status: ✅ Completed

A Binary Search Tree, a self-balancing AVL Tree, a Min-Heap, and a Hash Table with chaining, all storing city location records. Each structure is benchmarked at 100, 1,000, and 10,000 records against the others, comparing theoretical Big-O bounds to measured wall-clock performance for insertion, search, and deletion.

**Concepts covered:** BST and AVL rotations, heap sift-up/sift-down, hash collision handling and dynamic resizing, empirical complexity analysis.

**Run:**
```
cd task1
python3 bst.py
python3 avl.py
python3 min_heap.py
python3 hash_table.py
python3 benchmark.py
```

---

### Task 2 — Graph Algorithms and Pathfinding

> Status: ✅ Completed

The transportation network modelled as a weighted directed graph using an adjacency list. Dijkstra's algorithm computes shortest paths, Prim's algorithm builds a minimum spanning tree over an undirected copy of the network, and Bellman-Ford handles negative weights and detects negative cycles. All three are benchmarked on sparse and dense random graphs at increasing size.

**Concepts covered:** adjacency list representation, heap-based shortest path and MST construction, edge relaxation, negative cycle detection, dense vs sparse complexity trade-offs.

**Run:**
```
cd task2
python3 graph.py
python3 dijkstra.py
python3 prim.py
python3 bellman_ford.py
python3 benchmark.py
```

---

### Task 3 — Algorithmic Strategies for Complex Problems

> Status: ✅ Completed

Three paradigms applied to three separate problems from the approved coursework lists: Weighted Job Scheduling solved with bottom-up dynamic programming, Minimum Number of Platforms solved with a greedy sweep, and Hamiltonian Path solved with pruned backtracking. Each is benchmarked against a brute-force or naive baseline of worse complexity to show the practical payoff of the chosen approach.

**Concepts covered:** DP recurrence relations and bottom-up tables, greedy choice proofs, backtracking with pruning, exponential worst-case behaviour.

**Run:**
```
cd task3
python3 weighted_job_scheduling.py
python3 min_platforms.py
python3 hamiltonian_path.py
python3 benchmark.py
```

---

### Task 4 — NP-Hard Problem and Heuristics

> Status: ✅ Completed

The Vehicle Routing Problem with Time Windows (VRPTW), shown to be NP-Hard via reduction from the Travelling Salesman Problem. Two heuristics are implemented: a greedy nearest-feasible-neighbour construction, and a 2-opt local search that improves on it. Both are compared on solution quality and runtime across problem sizes from 10 to 100 customers.

**Concepts covered:** NP-Hardness reduction argument, greedy construction heuristics, 2-opt local search, solution quality vs runtime trade-off.

**Run:**
```
cd task4
python3 greedy_heuristic.py
python3 local_search.py
python3 benchmark.py
```

---

### Task 5 — Concurrent Programming

> Status: ✅ Completed

A parallel version of merge sort applied to the Task 1 city dataset. Python's Global Interpreter Lock prevents real CPU parallelism from threads, so this uses `multiprocessing` instead, splitting the dataset into per-worker chunks sorted independently and merged with a k-way merge. A shared progress counter protected by a `multiprocessing.Lock` demonstrates a proper critical section. Benchmarked at 1, 2, 4, and 8 workers to analyse scalability and synchronisation overhead.

**Concepts covered:** process-based parallelism, mutex-protected critical sections, k-way merge, Amdahl's Law, thread/process creation and communication overhead.

**Run:**
```
cd task5
python3 sequential_sort.py
python3 parallel_sort.py
python3 benchmark.py
```

---

## Documentation

Full write-ups for each task, including design justification, pseudocode, complexity analysis, experimental results, and critical discussion, are available in the accompanying assignment report:

- Task 1: Design rationale for each structure, Big-O and hidden constant analysis, empirical benchmarks at 100/1,000/10,000 records
- Task 2: Adjacency list justification, algorithm comparison on sparse vs dense graphs, negative weight handling
- Task 3: Recurrence relations, greedy choice proof, pruning strategy, complexity comparison against brute-force baselines
- Task 4: NP-Hardness argument, heuristic implementation, solution quality vs runtime evaluation
- Task 5: Synchronisation strategy, speedup analysis, overhead discussion (process creation, communication cost, Amdahl's Law)

---

## References

- Cormen, Leiserson, Rivest, and Stein, *Introduction to Algorithms*, for complexity bounds and algorithm design used throughout
- Python official documentation, `heapq` and `multiprocessing` modules
- Module lecture material, ST5003CEM Advanced Algorithms