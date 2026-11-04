"""
Experiment 3 (Binary Search) - Problem 1: Sqrt(x)
Link: https://leetcode.com/problems/sqrtx

Return the square root of x rounded down to the nearest integer, without using
built-in exponent functions.

Approach: binary search on the answer in [0, x]; find the largest m with m*m <= x.
Time: O(log x)   Space: O(1)
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi, ans = 0, x, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid <= x:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.mySqrt(0) == 0
    assert s.mySqrt(1) == 1
    assert s.mySqrt(4) == 2
    assert s.mySqrt(8) == 2
    assert s.mySqrt(2147395599) == 46339
    print("All tests passed")
