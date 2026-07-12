"""
Minimum Number of Platforms.
Given arrival and departure times at a station, find the minimum
number of platforms needed so no train waits. Greedy sweep over
sorted arrival/departure events. O(n log n).
"""


def min_platforms(arrivals, departures):
    arrivals = sorted(arrivals)
    departures = sorted(departures)
    n = len(arrivals)

    platforms_needed = 0
    max_platforms = 0
    i = j = 0

    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:
            platforms_needed -= 1
            j += 1

    return max_platforms


if __name__ == "__main__":
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]

    print("=" * 50)
    print("MINIMUM PLATFORMS - DEMO")
    print("=" * 50)

    print("\nTrain Schedule (arrival, departure):")
    for a, d in zip(arrivals, departures):
        print(f"  {a} -> {d}")

    result = min_platforms(arrivals, departures)
    print(f"\nMinimum Platforms Required: {result}")

    # Exact comparison: brute-force overlap count for verification
    def brute_force(arrivals, departures):
        n = len(arrivals)
        best = 0
        for t in arrivals:
            count = sum(1 for i in range(n) if arrivals[i] <= t <= departures[i])
            best = max(best, count)
        return best

    print(f"Brute-force Verification: {brute_force(arrivals, departures)}")