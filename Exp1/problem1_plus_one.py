"""
Experiment 1 (Arrays) - Problem 1: Plus One
Link: https://leetcode.com/problems/plus-one

Given a large integer as an array of digits, increment it by one
and return the resulting array.

Approach: walk from the last digit; a digit < 9 is simply incremented and we
stop, a 9 becomes 0 and the carry moves left. If every digit was 9, prepend 1.
Time: O(n)   Space: O(1) (O(n) only in the all-9s case)
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    s = Solution()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert s.plusOne([9]) == [1, 0]
    assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    print("All tests passed")
