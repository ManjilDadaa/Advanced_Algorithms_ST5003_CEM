"""
Sequential merge sort, used as the baseline for Task 5's concurrent
version. Sorts city records (from Task 1) by their distance field.
O(n log n) time, O(n) space.
"""

import random


class City:
    __slots__ = ("name", "distance")

    def __init__(self, name, distance):
        self.name = name
        self.distance = distance

    def __repr__(self):
        return f"City({self.name}, dist={self.distance:.2f})"


def generate_cities(n, seed=42):
    random.seed(seed)
    return [City(f"city_{i}", random.uniform(0, 10000)) for i in range(n)]


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i].distance <= right[j].distance:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort(cities):
    if len(cities) <= 1:
        return cities
    mid = len(cities) // 2
    left = merge_sort(cities[:mid])
    right = merge_sort(cities[mid:])
    return merge(left, right)


if __name__ == "__main__":
    cities = generate_cities(20)

    print("=" * 50)
    print("SEQUENTIAL MERGE SORT - DEMO")
    print("=" * 50)

    print("\nBefore Sorting (first 5):")
    for c in cities[:5]:
        print(f"  {c}")

    sorted_cities = merge_sort(cities)

    print("\nAfter Sorting (first 5, by distance):")
    for c in sorted_cities[:5]:
        print(f"  {c}")

    is_sorted = all(sorted_cities[i].distance <= sorted_cities[i + 1].distance
                     for i in range(len(sorted_cities) - 1))
    print(f"\nSorted Correctly: {is_sorted}")