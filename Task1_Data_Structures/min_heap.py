"""
Min-Heap (binary heap, array-backed) for priority queue operations,
e.g. selecting the next nearest city to visit by distance.
"""

from bst import City  # reuse City class


class MinHeap:
    def __init__(self):
        self._heap = []  # list of (priority, City)

    def __len__(self):
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0

    # ---------- Insert: O(log n) ----------
    def push(self, priority, city):
        self._heap.append((priority, city))
        self._sift_up(len(self._heap) - 1)

    # ---------- Extract-min: O(log n) ----------
    def pop(self):
        if not self._heap:
            raise IndexError("pop from empty heap")
        top = self._heap[0]
        last = self._heap.pop()
        if self._heap:
            self._heap[0] = last
            self._sift_down(0)
        return top  # (priority, city)

    # ---------- Peek: O(1) ----------
    def peek(self):
        if not self._heap:
            raise IndexError("peek at empty heap")
        return self._heap[0]

    # ---------- Decrease-key: O(n) search + O(log n) sift (used for "next nearest city") ----------
    def decrease_priority(self, city_name, new_priority):
        for i, (_, city) in enumerate(self._heap):
            if city.name == city_name:
                old_priority, city_obj = self._heap[i]
                if new_priority < old_priority:
                    self._heap[i] = (new_priority, city_obj)
                    self._sift_up(i)
                return True
        return False

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self._heap[i][0] < self._heap[parent][0]:
                self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = len(self._heap)
        while True:
            left, right = 2 * i + 1, 2 * i + 2
            smallest = i
            if left < n and self._heap[left][0] < self._heap[smallest][0]:
                smallest = left
            if right < n and self._heap[right][0] < self._heap[smallest][0]:
                smallest = right
            if smallest == i:
                break
            self._heap[i], self._heap[smallest] = self._heap[smallest], self._heap[i]
            i = smallest


if __name__ == "__main__":
    heap = MinHeap()
    cities = [
        ("Kathmandu", 0),
        ("Pokhara", 200),
        ("Butwal", 280),
        ("Biratnagar", 400),
        ("Dharan", 370),
    ]

    print("=" * 50)
    print("MIN-HEAP - DEMO")
    print("=" * 50)

    print("\nInsertion:")
    for name, dist in cities:
        heap.push(dist, City(name, 0, 0, 0, dist))
        print(f"  Inserted -> {name:<12} dist={dist}")

    print(f"\nHeap Size: {len(heap)}")

    print("\nPeek:")
    priority, city = heap.peek()
    print(f"  Next nearest -> {city.name} (dist={priority})")

    print("\nDecrease-Priority:")
    updated = heap.decrease_priority("Dharan", 50)
    status = "UPDATED" if updated else "NOT FOUND"
    print(f"  Dharan       -> {status} (new dist=50)")

    print("\nExtraction (pop order):")
    while not heap.is_empty():
        priority, city = heap.pop()
        print(f"  Visit -> {city.name:<12} dist={priority}")

    print(f"\nHeap Size: {len(heap)}")
    print("=" * 50)