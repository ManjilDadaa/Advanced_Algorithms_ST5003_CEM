"""
Hash Table with separate chaining for fast O(1) average-case city lookups.
Resizes (doubles) when load factor exceeds 0.75.
"""

from bst import City  # reuse City class


class HashTable:
    def __init__(self, capacity=16):
        self._capacity = capacity
        self._size = 0
        self._buckets = [[] for _ in range(self._capacity)]

    def __len__(self):
        return self._size

    def _hash(self, key):
        return hash(key) % self._capacity

    def _load_factor(self):
        return self._size / self._capacity

    def _resize(self):
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for bucket in old_buckets:
            for key, city in bucket:
                self.insert(key, city)

    # ---------- Insert: O(1) average, O(n) worst-case (all collisions) ----------
    def insert(self, key, city):
        if self._load_factor() >= 0.75:
            self._resize()
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, city)  # update
                return
        bucket.append((key, city))
        self._size += 1

    # ---------- Search: O(1) average, O(n) worst-case ----------
    def search(self, key):
        idx = self._hash(key)
        for k, city in self._buckets[idx]:
            if k == key:
                return city
        return None

    # ---------- Delete: O(1) average, O(n) worst-case ----------
    def delete(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return True
        return False

    def keys(self):
        return [k for bucket in self._buckets for k, _ in bucket]

    def max_chain_length(self):
        return max((len(b) for b in self._buckets), default=0)


if __name__ == "__main__":
    ht = HashTable()
    cities = [
        City("Kathmandu", 27.7172, 85.3240, 1_500_000, 0),
        City("Pokhara", 28.2096, 83.9856, 400_000, 200),
        City("Butwal", 27.7000, 83.4486, 150_000, 280),
        City("Biratnagar", 26.4525, 87.2718, 250_000, 400),
        City("Dharan", 26.8065, 87.2846, 150_000, 370),
    ]

    print("=" * 50)
    print("HASH TABLE - DEMO")
    print("=" * 50)

    print("\nInsertion:")
    for c in cities:
        ht.insert(c.name, c)
        print(f"  Inserted -> {c.name}")

    print(f"\nTotal Entries: {len(ht)}")
    print(f"Max Chain Length: {ht.max_chain_length()}")

    print("\nSearch:")
    for name in ["Pokhara", "Itahari"]:
        result = ht.search(name)
        status = "FOUND" if result else "NOT FOUND"
        print(f"  {name:<12} -> {status}")

    print("\nDeletion:")
    for name in ["Butwal", "Itahari"]:
        deleted = ht.delete(name)
        status = "DELETED" if deleted else "NOT FOUND"
        print(f"  {name:<12} -> {status}")

    print("\nRemaining Keys:")
    for key in ht.keys():
        print(f"  {key}")

    print(f"\nTotal Entries: {len(ht)}")
    print("=" * 50)