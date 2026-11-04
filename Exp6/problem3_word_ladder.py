"""
Experiment 6 (Hashing) - Problem 3: Word Ladder
Link: https://leetcode.com/problems/word-ladder

Given a start word, an end word and a dictionary, find the length of the
shortest transformation sequence where one letter changes at a time and every
intermediate word is in the dictionary.

Approach: BFS. A hash map groups words by wildcard pattern ("h*t") so all
one-letter neighbours are found in O(L) per word.
Time: O(N * L^2)   Space: O(N * L)
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        L = len(beginWord)
        patterns = defaultdict(list)
        for w in words | {beginWord}:
            for i in range(L):
                patterns[w[:i] + "*" + w[i + 1:]].append(w)

        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(L):
                for nxt in patterns[word[:i] + "*" + word[i + 1:]]:
                    if nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, dist + 1))
        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    print("All tests passed")
