"""
Beyond Syllabus (Fenwick Trees / Segment Trees) - Segment Tree (iterative, sum)

Classic usage: LeetCode 307 - Range Sum Query - Mutable
https://leetcode.com/problems/range-sum-query-mutable/

Segment tree supports:
  update(i, val)    - point update                    O(log n)
  query(l, r)       - sum over the inclusive range    O(log n)
Change the combine operation (+) to min / max / gcd to get other range queries.
"""
from typing import List


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i, v in enumerate(nums):  # leaves live at [n, 2n)
            self.tree[self.n + i] = v
        for i in range(self.n - 1, 0, -1):  # build internal nodes
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, i: int, val: int) -> None:
        i += self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def query(self, left: int, right: int) -> int:
        """Sum of nums[left..right] (inclusive)."""
        total = 0
        lo, hi = left + self.n, right + self.n + 1  # half-open [lo, hi)
        while lo < hi:
            if lo & 1:
                total += self.tree[lo]
                lo += 1
            if hi & 1:
                hi -= 1
                total += self.tree[hi]
            lo //= 2
            hi //= 2
        return total


if __name__ == "__main__":
    st = SegmentTree([1, 3, 5])
    assert st.query(0, 2) == 9
    st.update(1, 2)
    assert st.query(0, 2) == 8
    arr = list(range(1, 51))
    st = SegmentTree(arr)
    for l in range(0, 50, 3):
        for r in range(l, 50, 5):
            assert st.query(l, r) == sum(arr[l:r + 1])
    st.update(10, 1000)
    arr[10] = 1000
    assert st.query(5, 20) == sum(arr[5:21])
    print("All tests passed")
