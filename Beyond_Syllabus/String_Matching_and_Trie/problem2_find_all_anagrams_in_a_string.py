"""
Beyond Syllabus (String Matching and Trie) - Problem 2: Find All Anagrams in a String
Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given strings s and p, return an array of all the start indices of p's anagrams
in s (any order).

Approach: fixed-size sliding window of length len(p); compare character counts.
Time: O(n * 26)   Space: O(26)
"""
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        if m > len(s):
            return []
        need = Counter(p)
        window = Counter(s[:m])
        res = [0] if window == need else []
        for i in range(m, len(s)):
            window[s[i]] += 1
            out = s[i - m]
            window[out] -= 1
            if window[out] == 0:
                del window[out]
            if window == need:
                res.append(i - m + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert s.findAnagrams("abab", "ab") == [0, 1, 2]
    assert s.findAnagrams("a", "ab") == []
    print("All tests passed")
