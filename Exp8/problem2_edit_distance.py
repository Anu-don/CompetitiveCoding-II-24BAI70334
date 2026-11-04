"""
Experiment 8 (Dynamic Programming) - Problem 2: Edit Distance
Link: https://leetcode.com/problems/edit-distance/

Return the minimum number of insert, delete or replace operations needed to
convert word1 into word2.

Approach: dp[i][j] = edit distance between word1[:i] and word2[:j].
If the characters match: dp[i-1][j-1]; otherwise 1 + min(insert, delete, replace).
Time: O(m * n)   Space: O(m * n)
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i  # delete all characters
        for j in range(n + 1):
            dp[0][j] = j  # insert all characters
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j],      # delete
                                       dp[i][j - 1],      # insert
                                       dp[i - 1][j - 1])  # replace
        return dp[m][n]


if __name__ == "__main__":
    s = Solution()
    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("intention", "execution") == 5
    assert s.minDistance("", "abc") == 3
    assert s.minDistance("abc", "abc") == 0
    print("All tests passed")
