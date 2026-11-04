"""
Experiment 7 (Sliding Window) - Problem 1: Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i

Find a contiguous subarray of length k with the maximum average value.

Approach: fixed-size sliding window sum; add the new element, remove the old one.
Time: O(n)   Space: O(1)
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k])
        best = window
        for i in range(k, len(nums)):
            window += nums[i] - nums[i - k]
            best = max(best, window)
        return best / k


if __name__ == "__main__":
    s = Solution()
    assert abs(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-5
    assert abs(s.findMaxAverage([5], 1) - 5.0) < 1e-5
    print("All tests passed")
