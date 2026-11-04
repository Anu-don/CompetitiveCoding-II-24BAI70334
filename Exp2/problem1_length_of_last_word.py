"""
Experiment 2 (Strings) - Problem 1: Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word

Given a string of words and spaces, return the length of the last word.

Approach: scan from the right, skip trailing spaces, then count letters.
Time: O(n)   Space: O(1)
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLastWord("Hello World") == 5
    assert s.lengthOfLastWord("   fly me   to   the moon  ") == 4
    assert s.lengthOfLastWord("luffy is still joyboy") == 6
    print("All tests passed")
