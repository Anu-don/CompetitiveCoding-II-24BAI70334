"""
Experiment 2 (Strings) - Problem 2: Generate Parentheses
Link: https://leetcode.com/problems/generate-parentheses

Given n pairs of parentheses, generate all combinations of well-formed
parentheses.

Approach: backtracking. Add '(' while opens < n, add ')' while closes < opens.
Time: O(4^n / sqrt(n)) (Catalan number)   Space: O(n) recursion depth
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur: str, opened: int, closed: int) -> None:
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if opened < n:
                backtrack(cur + "(", opened + 1, closed)
            if closed < opened:
                backtrack(cur + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.generateParenthesis(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert s.generateParenthesis(1) == ["()"]
    assert len(s.generateParenthesis(4)) == 14
    print("All tests passed")
