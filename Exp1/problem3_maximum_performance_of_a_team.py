"""
Experiment 1 (Arrays) - Problem 3: Maximum Performance of a Team
Link: https://leetcode.com/problems/maximum-performance-of-a-team/

Given n engineers with speeds and efficiencies, select at most k engineers to
maximize team performance = (sum of speeds) * (min efficiency).

Approach: sort engineers by efficiency (descending). Treat the current engineer
as the minimum efficiency and keep the k largest speeds seen so far in a
min-heap.
Time: O(n log n)   Space: O(k)
"""
import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        engineers = sorted(zip(efficiency, speed), reverse=True)
        heap, total, best = [], 0, 0
        for eff, spd in engineers:
            heapq.heappush(heap, spd)
            total += spd
            if len(heap) > k:
                total -= heapq.heappop(heap)
            best = max(best, total * eff)
        return best % MOD


if __name__ == "__main__":
    s = Solution()
    assert s.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60
    assert s.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3) == 68
    assert s.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4) == 72
    print("All tests passed")
