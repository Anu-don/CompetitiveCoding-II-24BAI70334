"""
Experiment 5 (Heap / Priority Queue) - Problem 2: Task Scheduler
Link: https://leetcode.com/problems/task-scheduler

Given CPU tasks labeled A-Z and a cooldown n between identical tasks, return the
minimum number of CPU intervals needed to complete all tasks.

Approach (max-heap simulation): in each cycle of n+1 slots, run the most
frequent remaining tasks first; idle time appears only if fewer than n+1
distinct tasks are available.
Time: O(T log 26)   Space: O(26)
"""
import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [-c for c in Counter(tasks).values()]
        heapq.heapify(heap)
        cooling = deque()  # (ready_time, remaining_count)
        time = 0
        while heap or cooling:
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1  # one execution done (counts are negative)
                if cnt:
                    cooling.append((time + n, cnt))
            if cooling and cooling[0][0] == time:
                heapq.heappush(heap, cooling.popleft()[1])
        return time


if __name__ == "__main__":
    s = Solution()
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert s.leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10
    print("All tests passed")
