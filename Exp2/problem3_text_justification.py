"""
Experiment 2 (Strings) - Problem 3: Text Justification
Link: https://leetcode.com/problems/text-justification

Given an array of words and a max line width, format the text so each line is
fully justified with exactly maxWidth characters.

Approach: greedily pack as many words as fit on a line. For normal lines,
distribute the extra spaces as evenly as possible (extra goes to the left gaps).
The last line and single-word lines are left-justified.
Time: O(total characters)   Space: O(maxWidth)
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i, n = 0, len(words)
        while i < n:
            j, length = i, 0
            # words[i..j-1] fit, counting one space between each pair
            while j < n and length + len(words[j]) + (j - i) <= maxWidth:
                length += len(words[j])
                j += 1
            gaps = j - i - 1
            if j == n or gaps == 0:  # last line or single word -> left justify
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                spaces = maxWidth - length
                each, extra = divmod(spaces, gaps)
                line = ""
                for k in range(i, j - 1):
                    line += words[k] + " " * (each + (1 if k - i < extra else 0))
                line += words[j - 1]
            res.append(line)
            i = j
        return res


if __name__ == "__main__":
    s = Solution()
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    assert s.fullJustify(words, 16) == ["This    is    an", "example  of text", "justification.  "]
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    assert s.fullJustify(words, 16) == ["What   must   be", "acknowledgment  ", "shall be        "]
    print("All tests passed")
