"""
Experiment 5 (Heap / Priority Queue) - Problem 3: Sliding Window Maximum
Link: https://leetcode.com/problems/sliding-window-maximum

Given an integer array and a sliding window of size k, return the maximum value
in each window position.

Approach: monotonic deque of indices whose values are in decreasing order; the
front always holds the window maximum.
Time: O(n)   Space: O(k)
"""
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # indices, values decreasing
        res = []
        for i, x in enumerate(nums):
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:  # front fell out of the window
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert s.maxSlidingWindow([1], 1) == [1]
    assert s.maxSlidingWindow([9, 11], 2) == [11]
    print("All tests passed")
