"""
Experiment 7 (Sliding Window) - Problem 3: Sliding Window Median
Link: https://leetcode.com/problems/sliding-window-median

For each sliding window of size k, find the median of the elements present and
return all median values.

Approach: keep the current window in a sorted list. Use bisect to remove the
outgoing element and insert the incoming one; the median is read from the middle.
Time: O(n * k) worst case (list insert/remove), fast in practice   Space: O(k)
"""
import bisect
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        res = []
        for i in range(k, len(nums) + 1):
            if k % 2:
                res.append(float(window[k // 2]))
            else:
                res.append((window[k // 2 - 1] + window[k // 2]) / 2)
            if i == len(nums):
                break
            window.pop(bisect.bisect_left(window, nums[i - k]))
            bisect.insort(window, nums[i])
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [1, -1, -1, 3, 5, 6]
    assert s.medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], 3) == [2, 3, 3, 3, 2, 3, 2]
    assert s.medianSlidingWindow([1, 4, 2, 3], 4) == [2.5]
    print("All tests passed")
