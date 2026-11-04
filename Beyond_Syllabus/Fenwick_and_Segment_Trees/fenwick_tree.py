"""
Beyond Syllabus (Fenwick Trees / Segment Trees) - Fenwick Tree (Binary Indexed Tree)

NOTE: In the syllabus PDF, the three problems listed under this topic are
copies of the String Matching problems (Minimum Window Substring, Find All
Anagrams, Word Search II). They are already solved in
Beyond_Syllabus/String_Matching_and_Trie/. This file and segment_tree.py give
the actual Fenwick / Segment tree data structures with a classic usage
(LeetCode 307 - Range Sum Query - Mutable:
https://leetcode.com/problems/range-sum-query-mutable/).

Fenwick tree supports:
  update(i, delta)  - add delta to element i        O(log n)
  query(i)          - prefix sum of first i+1 items  O(log n)
  range_sum(l, r)   - sum of nums[l..r]              O(log n)
"""
from typing import List


class FenwickTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)
        for i, v in enumerate(nums):
            self._add(i + 1, v)

    def _add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # move to next responsible node

    def update(self, i: int, val: int) -> None:
        """Set nums[i] = val."""
        self._add(i + 1, val - self.nums[i])
        self.nums[i] = val

    def query(self, i: int) -> int:
        """Prefix sum nums[0..i]."""
        i += 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & (-i)  # drop the lowest set bit
        return total

    def range_sum(self, left: int, right: int) -> int:
        return self.query(right) - (self.query(left - 1) if left > 0 else 0)


if __name__ == "__main__":
    ft = FenwickTree([1, 3, 5])
    assert ft.range_sum(0, 2) == 9
    ft.update(1, 2)
    assert ft.range_sum(0, 2) == 8
    assert ft.range_sum(1, 2) == 7
    big = list(range(1, 101))
    ft = FenwickTree(big)
    for l in range(0, 100, 7):
        for r in range(l, 100, 11):
            assert ft.range_sum(l, r) == sum(big[l:r + 1])
    print("All tests passed")
