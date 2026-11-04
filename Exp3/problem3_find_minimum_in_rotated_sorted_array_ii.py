"""
Experiment 3 (Binary Search) - Problem 3: Find Minimum in Rotated Sorted Array II
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

Given a rotated sorted array with possible duplicates, find the minimum element.

Approach: compare nums[mid] with nums[hi]. If bigger, the minimum is to the
right; if smaller, it is at mid or to the left; if equal we cannot decide, so
drop hi by one.
Time: O(log n) average, O(n) worst case   Space: O(1)
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[lo]


if __name__ == "__main__":
    s = Solution()
    assert s.findMin([1, 3, 5]) == 1
    assert s.findMin([2, 2, 2, 0, 1]) == 0
    assert s.findMin([10, 1, 10, 10, 10]) == 1
    assert s.findMin([3, 1, 3]) == 1
    print("All tests passed")
