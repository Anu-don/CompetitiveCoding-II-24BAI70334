"""
Experiment 9 (Trees) - Problem 3: Sum of Distances in Tree
Link: https://leetcode.com/problems/sum-of-distances-in-tree

Given an undirected tree of n nodes, return an array where entry i is the sum of
distances from node i to all other nodes.

Approach: re-rooting DP.
  1. Root at 0. Compute subtree sizes and ans[0] (sum of distances from root).
  2. Move the root from parent p to child c:
        ans[c] = ans[p] - size[c] + (n - size[c])
     (nodes in c's subtree get 1 closer, all others get 1 farther).
Iterative (BFS order) so deep trees do not overflow the recursion limit.
Time: O(n)   Space: O(n)
"""
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        parent = [-1] * n
        order = [0]
        for u in order:  # BFS order; list grows while iterating
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)

        size = [1] * n
        ans = [0] * n
        for u in reversed(order):  # children before parents
            p = parent[u]
            if p != -1:
                size[p] += size[u]
                ans[p] += ans[u] + size[u]

        for u in order[1:]:  # parents before children
            ans[u] = ans[parent[u]] - size[u] + (n - size[u])
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]) == [8, 12, 6, 10, 10, 10]
    assert s.sumOfDistancesInTree(1, []) == [0]
    assert s.sumOfDistancesInTree(2, [[1, 0]]) == [1, 1]
    print("All tests passed")
