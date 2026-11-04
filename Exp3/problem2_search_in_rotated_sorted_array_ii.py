"""
Experiment 3 (Binary Search) - Problem 2: Search in Rotated Sorted Array II
Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii

Given a rotated sorted array that may contain duplicates, determine whether a
target value exists.

Approach: modified binary search. When nums[lo] == nums[mid] == nums[hi] we
cannot tell which half is sorted, so shrink both ends. Otherwise one half is
always sorted - check whether the target lies inside it.
Time: O(log n) average, O(n) worst case (many duplicates)   Space: O(1)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            if nums[lo] == nums[mid] == nums[hi]:
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]:  # left half sorted
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:  # right half sorted
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.search([2, 5, 6, 0, 0, 1, 2], 0) is True
    assert s.search([2, 5, 6, 0, 0, 1, 2], 3) is False
    assert s.search([1, 0, 1, 1, 1], 0) is True
    assert s.search([1], 0) is False
    print("All tests passed")
