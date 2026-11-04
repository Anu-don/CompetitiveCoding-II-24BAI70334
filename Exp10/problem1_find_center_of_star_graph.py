"""
Experiment 10 (Graphs) - Problem 1: Find Center of Star Graph
Link: https://leetcode.com/problems/find-center-of-star-graph/

Given an undirected star graph, identify and return the center node that is
directly connected to all other nodes.

Approach: the center appears in every edge, so it is the common node of any two
edges.
Time: O(1)   Space: O(1)
"""
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a, b = edges[0]
        return a if a in edges[1] else b


if __name__ == "__main__":
    s = Solution()
    assert s.findCenter([[1, 2], [2, 3], [4, 2]]) == 2
    assert s.findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]) == 1
    print("All tests passed")
