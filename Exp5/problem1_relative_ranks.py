"""
Experiment 5 (Heap / Priority Queue) - Problem 1: Relative Ranks
Link: https://leetcode.com/problems/relative-ranks

Given unique athlete scores, rank them: highest -> "Gold Medal", second ->
"Silver Medal", third -> "Bronze Medal", the rest -> their placement number.

Approach: build a max-heap of (score, index) and pop in order of rank.
Time: O(n log n)   Space: O(n)
"""
import heapq
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)
        res = [""] * len(score)
        rank = 1
        while heap:
            _, i = heapq.heappop(heap)
            res[i] = medals[rank - 1] if rank <= 3 else str(rank)
            rank += 1
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.findRelativeRanks([5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    assert s.findRelativeRanks([10, 3, 8, 9, 4]) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
    print("All tests passed")
