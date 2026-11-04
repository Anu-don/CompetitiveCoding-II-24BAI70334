"""
Experiment 4 (Monotonic Stack) - Problem 3: Create Maximum Number
Link: https://leetcode.com/problems/create-maximum-number/

Create the maximum number of length k from the digits of two arrays,
preserving the relative order of digits within each array.

Approach:
  1. For every split (i digits from nums1, k-i from nums2), pick the largest
     subsequence of the required length from each array using a monotonic stack.
  2. Merge the two subsequences into the lexicographically largest sequence.
  3. Keep the best result over all splits.
Time: O(k * (m + n + k))   Space: O(k)
"""
from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums: List[int], t: int) -> List[int]:
            """Largest subsequence of length t (monotonic stack)."""
            drop = len(nums) - t
            stack = []
            for d in nums:
                while drop and stack and stack[-1] < d:
                    stack.pop()
                    drop -= 1
                stack.append(d)
            return stack[:t]

        def merge(a: List[int], b: List[int]) -> List[int]:
            """Merge two sequences into the largest one.
            Comparing whole remaining lists breaks ties correctly."""
            a, b = a[:], b[:]
            out = []
            while a or b:
                bigger = a if a > b else b
                out.append(bigger.pop(0))
            return out

        best = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            cand = merge(pick(nums1, i), pick(nums2, k - i))
            if cand > best:
                best = cand
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxNumber([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5) == [9, 8, 6, 5, 3]
    assert s.maxNumber([6, 7], [6, 0, 4], 5) == [6, 7, 6, 0, 4]
    assert s.maxNumber([3, 9], [8, 9], 3) == [9, 8, 9]
    print("All tests passed")
