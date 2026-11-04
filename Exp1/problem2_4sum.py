"""
Experiment 1 (Arrays) - Problem 2: 4Sum
Link: https://leetcode.com/problems/4sum/

Given an array of n integers, return all unique quadruplets [a, b, c, d]
such that their sum equals the target.

Approach: sort, fix the first two numbers, then use two pointers for the rest,
skipping duplicate values at every level.
Time: O(n^3)   Space: O(1) extra (excluding output)
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo, hi = j + 1, n - 1
                while lo < hi:
                    total = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if total == target:
                        res.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
                    elif total < target:
                        lo += 1
                    else:
                        hi -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    out = s.fourSum([1, 0, -1, 0, -2, 2], 0)
    assert sorted(out) == sorted([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]])
    assert s.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    print("All tests passed")
