"""
Beyond Syllabus (String Matching and Trie) - Problem 1: Minimum Window Substring
Link: https://leetcode.com/problems/minimum-window-substring/

Given strings s and t, return the minimum window substring of s such that every
character in t (including duplicates) is included in the window. Return "" if no
such window exists.

Approach: variable sliding window. Expand right until all required characters
are covered, then shrink left as far as possible while keeping the window valid.
Time: O(m + n)   Space: O(1) (bounded alphabet)
"""
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t) > len(s):
            return ""
        need = Counter(t)
        missing = len(t)
        left = 0
        best_len, best_l = float("inf"), 0
        for right, ch in enumerate(s):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            while missing == 0:
                if right - left + 1 < best_len:
                    best_len, best_l = right - left + 1, left
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        return "" if best_len == float("inf") else s[best_l:best_l + best_len]


if __name__ == "__main__":
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("a", "a") == "a"
    assert s.minWindow("a", "aa") == ""
    print("All tests passed")
