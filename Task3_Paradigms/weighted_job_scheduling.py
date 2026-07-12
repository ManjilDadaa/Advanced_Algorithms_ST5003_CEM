"""
Weighted Job Scheduling with time windows.
Given jobs with (start, end, profit), select a non-overlapping subset
maximising total profit. Bottom-up DP with binary search for the
latest compatible job. O(n log n).
"""

from bisect import bisect_right


def latest_non_conflicting(jobs, i):
    """Binary search for the rightmost job ending <= jobs[i].start."""
    ends = [j[1] for j in jobs]
    idx = bisect_right(ends, jobs[i][0]) - 1
    return idx  # -1 if none


def weighted_job_scheduling(jobs):
    jobs = sorted(jobs, key=lambda j: j[1])  # sort by end time
    n = len(jobs)
    dp = [0] * (n + 1)  # dp[i] = best profit using first i jobs (sorted)

    for i in range(1, n + 1):
        job = jobs[i - 1]
        incl_profit = job[2] + dp[latest_non_conflicting(jobs, i - 1) + 1]
        dp[i] = max(dp[i - 1], incl_profit)

    return dp[n], dp, jobs


def weighted_job_scheduling_naive(jobs):
    """Same recurrence, but finds the latest non-conflicting job by a
    linear scan instead of binary search. O(n^2) overall, used only to
    demonstrate the practical benefit of the O(n log n) version."""
    jobs = sorted(jobs, key=lambda j: j[1])
    n = len(jobs)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        job = jobs[i - 1]
        p = -1
        for k in range(i - 1):  # linear scan instead of bisect
            if jobs[k][1] <= job[0]:
                p = k
        incl_profit = job[2] + dp[p + 1]
        dp[i] = max(dp[i - 1], incl_profit)

    return dp[n]


def reconstruct(dp, jobs):
    """Trace back which jobs were selected."""
    selected = []
    i = len(jobs)
    while i > 0:
        job = jobs[i - 1]
        incl_profit = job[2] + dp[latest_non_conflicting(jobs, i - 1) + 1]
        if incl_profit > dp[i - 1]:
            selected.append(job)
            i = latest_non_conflicting(jobs, i - 1) + 1
        else:
            i -= 1
    return list(reversed(selected))


if __name__ == "__main__":
    # (start, end, profit) - delivery jobs with time windows
    jobs = [
        (1, 3, 50),
        (2, 5, 20),
        (4, 6, 70),
        (6, 7, 60),
        (5, 8, 30),
        (7, 9, 40),
    ]

    print("=" * 50)
    print("WEIGHTED JOB SCHEDULING - DEMO")
    print("=" * 50)

    print("\nJobs (start, end, profit):")
    for j in jobs:
        print(f"  {j}")

    best_profit, dp, sorted_jobs = weighted_job_scheduling(jobs)
    selected = reconstruct(dp, sorted_jobs)

    print("\nDP Table:")
    for i, val in enumerate(dp):
        print(f"  dp[{i}] = {val}")

    print("\nSelected Jobs:")
    for j in selected:
        print(f"  {j}")

    print(f"\nMax Profit: {best_profit}")