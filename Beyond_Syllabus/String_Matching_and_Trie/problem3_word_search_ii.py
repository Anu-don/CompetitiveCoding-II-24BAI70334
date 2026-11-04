"""
Beyond Syllabus (String Matching and Trie) - Problem 3: Word Search II
Link: https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of words, return all words on the
board. Each word is built from sequentially adjacent (horizontal/vertical) cells
and a cell may not be reused within a word.

Approach: insert all words into a Trie, then DFS from every cell following the
Trie. Found words are cleared and exhausted branches are pruned to speed up.
Time: O(m * n * 4^L) worst case, heavily pruned by the Trie   Space: O(total word length)
"""
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                node = node.children.setdefault(ch, TrieNode())
            node.word = w

        m, n = len(board), len(board[0])
        res = []

        def dfs(r: int, c: int, parent: TrieNode) -> None:
            ch = board[r][c]
            node = parent.children.get(ch)
            if node is None:
                return
            if node.word:
                res.append(node.word)
                node.word = None  # avoid duplicates
            board[r][c] = "#"  # mark visited
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    dfs(nr, nc, node)
            board[r][c] = ch
            if not node.children and node.word is None:
                del parent.children[ch]  # prune dead branch

        for r in range(m):
            for c in range(n):
                dfs(r, c, root)
        return res


if __name__ == "__main__":
    s = Solution()
    board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    assert sorted(s.findWords(board, ["oath", "pea", "eat", "rain"])) == ["eat", "oath"]
    assert s.findWords([["a", "b"], ["c", "d"]], ["abcb"]) == []
    print("All tests passed")
