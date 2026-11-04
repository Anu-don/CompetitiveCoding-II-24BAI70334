"""
Beyond Syllabus (Advanced Graphs) - Problem 1: Critical Connections in a Network
Link: https://leetcode.com/problems/critical-connections-in-a-network/

Given an undirected network of n servers, a critical connection is an edge whose
removal disconnects the network. Return all such edges (bridges).

Approach: Tarjan's bridge-finding algorithm. disc[u] = discovery time,
low[u] = earliest discovery time reachable from u's subtree using one back edge.
Tree edge (u, v) is a bridge when low[v] > disc[u].
Time: O(V + E)   Space: O(V + E)
"""
import sys
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        sys.setrecursionlimit(max(10000, 2 * n + 100))
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        disc = [-1] * n
        low = [0] * n
        timer = [0]
        bridges = []

        def dfs(u: int, parent: int) -> None:
            disc[u] = low[u] = timer[0]
            timer[0] += 1
            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])

        for start in range(n):  # handles disconnected input safely
            if disc[start] == -1:
                dfs(start, -1)
        return bridges


if __name__ == "__main__":
    s = Solution()
    out = s.criticalConnections(4, [[0, 1], [1, 2], [2, 0], [1, 3]])
    assert sorted(sorted(e) for e in out) == [[1, 3]]
    assert s.criticalConnections(2, [[0, 1]]) == [[0, 1]]
    out = s.criticalConnections(5, [[0, 1], [1, 2], [2, 3], [3, 4]])
    assert len(out) == 4
    print("All tests passed")
