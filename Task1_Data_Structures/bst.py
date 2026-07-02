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


class BST:
    def __init__(self):
        self.root = None
        self._size = 0

    def __len__(self):
        return self._size

    # ---------- Insert: O(h), h = tree height (O(log n) avg, O(n) worst) ----------
    def insert(self, key, city):
        self.root = self._insert(self.root, key, city)

    def _insert(self, node, key, city):
        if node is None:
            self._size += 1
            return BSTNode(key, city)
        if key < node.key:
            node.left = self._insert(node.left, key, city)
        elif key > node.key:
            node.right = self._insert(node.right, key, city)
        else:
            node.city = city  # update existing
        return node

    # ---------- Search: O(h) ----------
    def search(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return node.city
            node = node.left if key < node.key else node.right
        return None

    # ---------- Delete: O(h) ----------
    def delete(self, key):
        self.root, deleted = self._delete(self.root, key)
        if deleted:
            self._size -= 1
        return deleted

    def _delete(self, node, key):
        if node is None:
            return node, False
        if key < node.key:
            node.left, deleted = self._delete(node.left, key)
        elif key > node.key:
            node.right, deleted = self._delete(node.right, key)
        else:
            deleted = True
            if node.left is None:
                return node.right, deleted
            if node.right is None:
                return node.left, deleted
            successor = self._min_node(node.right)
            node.key, node.city = successor.key, successor.city
            node.right, _ = self._delete(node.right, successor.key)
        return node, deleted

    def _min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    # ---------- Inorder traversal (sorted order) ----------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append((node.key, node.city))
            self._inorder(node.right, result)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))


if __name__ == "__main__":
    tree = BST()
    tree.insert("Kathmandu", City("Kathmandu", 27.7172, 85.3240, 1_500_000, 0))
    tree.insert("Pokhara", City("Pokhara", 28.2096, 83.9856, 400_000, 200))
    tree.insert("Butwal", City("Butwal", 27.7000, 83.4486, 150_000, 280))
    print(tree.search("Pokhara"))
    print("Inorder:", tree.inorder())
    print("Height:", tree.height())