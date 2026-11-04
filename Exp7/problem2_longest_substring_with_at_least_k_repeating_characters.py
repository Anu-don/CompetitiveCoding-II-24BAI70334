"""
Experiment 7 (Sliding Window) - Problem 2: Longest Substring with At Least K Repeating Characters
Link: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters

Return the length of the longest substring where every character appears at
least k times.

Approach: for each target number of unique characters (1..26) run a variable
sliding window that keeps exactly `unique <= target` distinct letters and counts
how many of them already appear >= k times. A window is valid when
unique == target == atLeastK.
Time: O(26 * n)   Space: O(26)
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        best = 0
        for target in range(1, 27):
            count = [0] * 26
            left = unique = at_least_k = 0
            for right, ch in enumerate(s):
                i = ord(ch) - 97
                if count[i] == 0:
                    unique += 1
                count[i] += 1
                if count[i] == k:
                    at_least_k += 1
                while unique > target:
                    j = ord(s[left]) - 97
                    if count[j] == k:
                        at_least_k -= 1
                    count[j] -= 1
                    if count[j] == 0:
                        unique -= 1
                    left += 1
                if unique == target and at_least_k == target:
                    best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.longestSubstring("aaabb", 3) == 3
    assert s.longestSubstring("ababbc", 2) == 5
    assert s.longestSubstring("a", 2) == 0
    assert s.longestSubstring("weitong", 2) == 0
    print("All tests passed")
