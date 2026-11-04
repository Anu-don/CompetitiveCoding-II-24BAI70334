"""
Experiment 10 (Graphs) - Problem 3: Redundant Connection II
Link: https://leetcode.com/problems/redundant-connection-ii/

A directed graph was formed by adding one extra edge to a rooted tree. Identify
and remove the redundant edge to restore a valid rooted tree (if several
answers exist, return the one that appears last in the input).

Approach: two possible problems - a node with two parents and/or a cycle.
  1. Find a node with two parents; the two edges into it are candidates
     (cand1 = earlier, cand2 = later).
  2. Run union-find while ignoring cand2.
     - A cycle still appears -> cand1 is the bad edge (or the cycle edge if
       there is no two-parent node).
     - No cycle -> cand2 is the answer.
Time: O(n * alpha(n))   Space: O(n)
"""
from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0] * (n + 1)
        cand1 = cand2 = None
        for u, v in edges:
            if parent[v]:
                cand1 = [parent[v], v]
                cand2 = [u, v]
            else:
                parent[v] = u

        uf = list(range(n + 1))

        def find(x: int) -> int:
            while uf[x] != x:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        for u, v in edges:
            if [u, v] == cand2:  # pretend this edge does not exist
                continue
            ru, rv = find(u), find(v)
            if ru == rv:  # cycle found
                return cand1 if cand1 else [u, v]
            uf[rv] = ru
        return cand2


if __name__ == "__main__":
    s = Solution()
    assert s.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert s.findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [4, 1]
    assert s.findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2], [1, 4]]) == [2, 1]
    print("All tests passed")
