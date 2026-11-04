"""
Experiment 8 (Dynamic Programming) - Problem 3: Longest Valid Parentheses
Link: https://leetcode.com/problems/longest-valid-parentheses/

Given a string of '(' and ')' characters, return the length of the longest
valid (well-formed) parentheses substring.

Approach (DP): dp[i] = length of the longest valid substring ending at index i.
  - s[i] == ')' and s[i-1] == '(' : dp[i] = dp[i-2] + 2
  - s[i] == ')' and s[i-1] == ')' : if the char before the matched block is '(',
    dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
Time: O(n)   Space: O(n)
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        best = 0
        for i in range(1, n):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                else:
                    j = i - dp[i - 1] - 1  # index just before the valid block ending at i-1
                    if j >= 0 and s[j] == "(":
                        dp[i] = dp[i - 1] + 2 + (dp[j - 1] if j >= 1 else 0)
                best = max(best, dp[i])
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.longestValidParentheses("(()") == 2
    assert s.longestValidParentheses(")()())") == 4
    assert s.longestValidParentheses("") == 0
    assert s.longestValidParentheses("()(())") == 6
    assert s.longestValidParentheses("((()))())") == 8
    print("All tests passed")
