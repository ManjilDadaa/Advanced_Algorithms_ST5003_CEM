"""
Heuristic 1: Greedy construction.
Builds routes by repeatedly extending the current route to the
nearest unvisited customer that keeps the route capacity- and
time-window-feasible. When no customer can be feasibly added, the
current route returns to the depot and a new route starts.
"""

from vrptw import distance, route_feasible, generate_instance, total_distance


def greedy_construct(customers, capacity):
    unvisited = set(c.id for c in customers if c.id != 0)
    routes = []

    while unvisited:
        route = [0]  # start at depot
        while True:
            current = customers[route[-1]]
            candidates = sorted(unvisited, key=lambda cid: distance(current, customers[cid]))
            added = False
            for cid in candidates:
                trial_route = route + [cid, 0]
                if route_feasible(trial_route, customers, capacity):
                    route.append(cid)
                    unvisited.remove(cid)
                    added = True
                    break
            if not added:
                break
        route.append(0)  # close route back at depot
        routes.append(route)

    return routes


if __name__ == "__main__":
    customers, capacity = generate_instance(n_customers=15)

    print("=" * 50)
    print("VRPTW GREEDY HEURISTIC - DEMO")
    print("=" * 50)

    print(f"\nCustomers: {len(customers) - 1}, Vehicle Capacity: {capacity}")

    routes = greedy_construct(customers, capacity)

    print("\nConstructed Routes:")
    for i, route in enumerate(routes):
        print(f"  Route {i + 1}: {route}")

    print(f"\nTotal Distance: {total_distance(routes, customers):.2f}")
    print(f"Vehicles Used: {len(routes)}")