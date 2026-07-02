"""
Binary Search Tree (unbalanced) for storing city locations.
Keyed by city name. Each node stores coordinates, population, distance.
"""

class City:
    def __init__(self, name, lat, lon, population, distance):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.population = population
        self.distance = distance

    def __repr__(self):
        return f"City({self.name}, pop={self.population}, dist={self.distance})"


class BSTNode:
    __slots__ = ("key", "city", "left", "right")

    def __init__(self, key, city):
        self.key = key
        self.city = city
        self.left = None
        self.right = None
