# ST5003CEM - Advanced Algorithms Coursework

Individual coursework implementing advanced data structures, graph algorithms, algorithmic paradigms, NP-hard heuristics, and concurrent programming.

**Module:** Advanced Algorithms (ST5003CEM)
**Credit:** 10 | **Word Count:** 2000 | **Pass mark:** 40%

---

## Project Structure

```
advanced-algorithms-cw/
├── task1_data_structures/
│   ├── bst.c
│   ├── avl.c
│   ├── min_heap.c
│   ├── hash_table.c
│   └── benchmark.c
├── task2_graph_algorithms/
│   ├── graph.c
│   ├── dijkstra.c
│   ├── prim.c
│   ├── bellman_ford.c
│   └── benchmark.c
├── task3_paradigms/
│   ├── dp_<chosen_problem>.c
│   ├── greedy_<chosen_problem>.c
│   └── backtracking_<chosen_problem>.c
├── task4_np_hard/
│   ├── <chosen_problem>.c
│   ├── heuristic1_<name>.c
│   └── heuristic2_<name>.c
├── task5_concurrent/
│   ├── sequential_version.c
│   ├── parallel_version.c
│   └── benchmark.c
├── results/
│   ├── graphs/
│   └── raw_data/
├── report/
│   └── NAME_studentID.docx
└── README.md
```

---

## Tasks Overview

### Task 1: Advanced Data Structures (25 marks)
- BST, AVL tree, Min-Heap, Hash Table for city location storage (coords, population, distance).
- Theoretical Big-O for insert/delete/search per structure + discuss constant factor.
- Empirical benchmarks at n = 100 / 1,000 / 10,000. Wall-clock timing.
- Compare theory vs actual (graphs + tables). Justify best structure per use case.

### Task 2: Graph Algorithms & Pathfinding (30 marks)
- Weighted directed graph model of transport network (adjacency list/matrix — justify).
- Dijkstra (shortest path), Prim's (MST), Bellman-Ford (negative weights + cycle detection).
- Compare time/space complexity, dense vs sparse suitability, negative-weight handling.
- Report Big-O **and** observed constant factor separately. Include execution visualisations.

### Task 3: Algorithmic Strategies (25 marks)
Pick ONE per paradigm from the approved lists:
- **DP (10 marks):** _[fill in chosen problem]_ — subproblems, recurrence, memo/tabulation strategy, complexity + hidden constant.
- **Greedy (7 marks):** _[fill in chosen problem]_ — state greedy choice, prove/disprove optimality, compare vs exact approach.
- **Backtracking (8 marks):** _[fill in chosen problem]_ — pruning strategy, exponential worst-case vs practical search space reduction.

### Task 4: NP-Hard Problem & Heuristics (10 marks)
- Chosen problem: _[fill in]_ — explain NP-hardness with a known reduction.
- Implement ≥2 heuristics (Greedy / Local Search / GRASP / Simulated Annealing).
- Compare solution quality vs runtime; discuss quality-cost trade-off.

### Task 5: Concurrent Programming (10 marks)
- Parallel version of one earlier algorithm (e.g. parallel BFS/DFS, concurrent Dijkstra, parallel sort).
- POSIX threads (pthreads); mutexes/semaphores/condition variables for sync.
- Identify critical sections, prevent race conditions.
- Speedup vs sequential at 1/2/4/8 threads; plot speedup vs thread count; explain overheads (locking, cache coherence, thread creation).

---

## Notes

- All 5 problem choices (Task 3 DP/Greedy/Backtracking, Task 4 NP-hard) must come from the approved lists only.
- Marking weighs: Implementation, Algorithm Design, Complexity Analysis, Academic Writing, Critical Evaluation.
- Report must be independent work — cite all sources, disclose any AI tool use per academic integrity policy.
