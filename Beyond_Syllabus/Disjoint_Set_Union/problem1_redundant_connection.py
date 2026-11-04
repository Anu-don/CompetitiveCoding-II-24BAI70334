"""
Beyond Syllabus (Disjoint Set Union) - Problem 1: Redundant Connection
Link: https://leetcode.com/problems/redundant-connection/

An undirected graph was originally a tree with n nodes but has one extra edge,
creating a cycle. Return the edge whose removal restores the tree; if several
edges work, return the last one in the input.

Approach: union-find. The first edge that connects two nodes already in the same
component closes the cycle.
Time: O(n * alpha(n))   Space: O(n)
"""
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return [a, b]
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("All tests passed")
