"""
Vehicle Routing Problem with Time Windows (VRPTW).
Multiple vehicles, each with a capacity limit, must serve a set of
customers with demand and a delivery time window, starting and
ending at a depot, minimising total travel distance.

VRPTW generalises the Travelling Salesman Problem: with one vehicle,
infinite capacity, and no time windows, it reduces exactly to TSP.
Since TSP is NP-Hard (via reduction from Hamiltonian Cycle, itself
NP-Complete), VRPTW is NP-Hard too, and strictly harder in general
since it adds capacity and time-window side constraints on top.
"""

import math
import random


class Customer:
    def __init__(self, cid, x, y, demand, ready, due, service=10):
        self.id = cid
        self.x = x
        self.y = y
        self.demand = demand
        self.ready = ready
        self.due = due
        self.service = service


def distance(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)


def generate_instance(n_customers, capacity=50, seed=42):
    random.seed(seed)
    depot = Customer(0, 50, 50, 0, 0, 100000)
    customers = [depot]
    for i in range(1, n_customers + 1):
        x, y = random.uniform(0, 100), random.uniform(0, 100)
        demand = random.randint(5, 15)
        ready = random.randint(0, 300)
        due = ready + random.randint(150, 300)  # generous window
        customers.append(Customer(i, x, y, demand, ready, due))
    return customers, capacity


def route_distance(route, customers):
    total = 0
    for i in range(len(route) - 1):
        total += distance(customers[route[i]], customers[route[i + 1]])
    return total


def route_feasible(route, customers, capacity):
    """Check capacity and time-window feasibility for a full route
    (a list of customer ids starting and ending at depot, id 0)."""
    load = sum(customers[cid].demand for cid in route if cid != 0)
    if load > capacity:
        return False
    t = 0
    for i in range(len(route) - 1):
        a, b = customers[route[i]], customers[route[i + 1]]
        t += distance(a, b)
        t = max(t, b.ready)  # wait if arriving early
        if t > b.due:
            return False
        t += b.service
    return True


def total_distance(routes, customers):
    return sum(route_distance(r, customers) for r in routes)