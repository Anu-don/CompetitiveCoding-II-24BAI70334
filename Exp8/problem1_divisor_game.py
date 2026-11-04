"""
Experiment 8 (Dynamic Programming) - Problem 1: Divisor Game
Link: https://leetcode.com/problems/divisor-game

Alice and Bob take turns choosing a divisor x of the current number n
(0 < x < n) and replacing n with n - x. The player who cannot move loses.
Determine if Alice (who starts) wins when both play optimally.

Approach (DP): dp[i] is True if the player to move wins with number i.
dp[i] = any(dp[i - x] is False) over divisors x of i.
(Pattern: Alice wins exactly when n is even - see the O(1) version.)
Time: O(n^2)   Space: O(n)
"""


class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(2, n + 1):
            for x in range(1, i):
                if i % x == 0 and not dp[i - x]:
                    dp[i] = True
                    break
        return dp[n]

    def divisorGameO1(self, n: int) -> bool:
        return n % 2 == 0


if __name__ == "__main__":
    s = Solution()
    assert s.divisorGame(2) is True
    assert s.divisorGame(3) is False
    for n in range(1, 60):
        assert s.divisorGame(n) == s.divisorGameO1(n)
    print("All tests passed")
