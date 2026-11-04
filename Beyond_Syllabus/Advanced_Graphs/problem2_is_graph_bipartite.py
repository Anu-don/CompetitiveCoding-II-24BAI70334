"""
Beyond Syllabus (Advanced Graphs) - Problem 2: Is Graph Bipartite?
Link: https://leetcode.com/problems/is-graph-bipartite/

Given an undirected graph as an adjacency list, return True if its nodes can be
split into two sets such that every edge connects one set to the other.

(Same problem as Experiment 10 / Problem 2; solved here with iterative DFS
colouring as an alternative to the BFS version.)

Approach: DFS 2-colouring on every component; a same-colour edge means the graph
contains an odd cycle and is not bipartite.
Time: O(V + E)   Space: O(V)
"""
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        for start in range(len(graph)):
            if color[start] != -1:
                continue
            color[start] = 0
            stack = [start]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
    assert s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True
    print("All tests passed")
