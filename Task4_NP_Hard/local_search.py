"""
Heuristic 2: Local search (2-opt).
Starts from the greedy construction and repeatedly reverses
segments within each route if doing so shortens it and keeps the
route feasible, stopping when no improving move remains (hill
climbing to a local optimum).
"""

from vrptw import route_distance, route_feasible, total_distance, generate_instance
from greedy_heuristic import greedy_construct


def two_opt(route, customers, capacity):
    improved = True
    best = route[:]
    best_dist = route_distance(best, customers)

    while improved:
        improved = False
        for i in range(1, len(best) - 2):
            for j in range(i + 1, len(best) - 1):
                candidate = best[:i] + best[i:j + 1][::-1] + best[j + 1:]
                if not route_feasible(candidate, customers, capacity):
                    continue
                candidate_dist = route_distance(candidate, customers)
                if candidate_dist < best_dist:
                    best, best_dist = candidate, candidate_dist
                    improved = True
        # loop again if any improving swap was applied this pass

    return best


def local_search(routes, customers, capacity):
    return [two_opt(route, customers, capacity) for route in routes]


if __name__ == "__main__":
    customers, capacity = generate_instance(n_customers=15)

    print("=" * 50)
    print("VRPTW LOCAL SEARCH (2-OPT) - DEMO")
    print("=" * 50)

    initial_routes = greedy_construct(customers, capacity)
    initial_dist = total_distance(initial_routes, customers)

    improved_routes = local_search(initial_routes, customers, capacity)
    improved_dist = total_distance(improved_routes, customers)

    print(f"\nGreedy Distance:      {initial_dist:.2f}")
    print(f"After 2-opt Distance: {improved_dist:.2f}")
    print(f"Improvement:          {initial_dist - improved_dist:.2f} "
          f"({(1 - improved_dist / initial_dist) * 100:.1f}%)")

    print("\nRoutes After 2-opt:")
    for i, route in enumerate(improved_routes):
        print(f"  Route {i + 1}: {route}")