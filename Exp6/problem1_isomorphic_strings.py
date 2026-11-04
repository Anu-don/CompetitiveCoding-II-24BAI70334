"""
Experiment 6 (Hashing) - Problem 1: Isomorphic Strings
Link: https://leetcode.com/problems/isomorphic-strings

Determine if two strings are isomorphic: characters in s can be replaced to get
t, with a one-to-one mapping (no two characters map to the same character).

Approach: two hash maps (s->t and t->s) must stay consistent.
Time: O(n)   Space: O(1) (bounded alphabet)
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_to_t, t_to_s = {}, {}
        for a, b in zip(s, t):
            if s_to_t.get(a, b) != b or t_to_s.get(b, a) != a:
                return False
            s_to_t[a] = b
            t_to_s[b] = a
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isIsomorphic("egg", "add") is True
    assert s.isIsomorphic("foo", "bar") is False
    assert s.isIsomorphic("paper", "title") is True
    assert s.isIsomorphic("badc", "baba") is False
    print("All tests passed")
