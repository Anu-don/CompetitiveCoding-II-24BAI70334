"""
Experiment 4 (Monotonic Stack) - Problem 2: Next Greater Element II
Link: https://leetcode.com/problems/next-greater-element-ii

Given a circular array, return the next greater number for every element,
searching circularly.

Approach: traverse indices 0 .. 2n-1 (using i % n) with a monotonic stack of
indices; only the first pass pushes new indices.
Time: O(n)   Space: O(n)
"""
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # indices with decreasing values
        for i in range(2 * n):
            x = nums[i % n]
            while stack and nums[stack[-1]] < x:
                res[stack.pop()] = x
            if i < n:
                stack.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.nextGreaterElements([1, 2, 1]) == [2, -1, 2]
    assert s.nextGreaterElements([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]
    print("All tests passed")
