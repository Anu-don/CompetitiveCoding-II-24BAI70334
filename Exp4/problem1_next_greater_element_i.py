"""
Experiment 4 (Monotonic Stack) - Problem 1: Next Greater Element I
Link: https://leetcode.com/problems/next-greater-element-i

For each element in nums1 (a subset of nums2), find the next greater element to
its right in nums2. Return -1 if none exists.

Approach: one pass over nums2 with a decreasing monotonic stack; when a bigger
value arrives, it is the answer for everything it pops. Store answers in a dict.
Time: O(n + m)   Space: O(n)
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt = {}
        stack = []
        for x in nums2:
            while stack and stack[-1] < x:
                nxt[stack.pop()] = x
            stack.append(x)
        return [nxt.get(x, -1) for x in nums1]


if __name__ == "__main__":
    s = Solution()
    assert s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert s.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    print("All tests passed")
