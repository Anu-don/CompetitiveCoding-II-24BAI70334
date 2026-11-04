"""
Experiment 10 (Graphs) - Problem 2: Is Graph Bipartite?
Link: https://leetcode.com/problems/is-graph-bipartite/

Determine whether an undirected graph is bipartite: can the nodes be split into
two sets so that no two adjacent nodes are in the same set?

Approach: BFS 2-colouring of every connected component. If an edge joins two
nodes of the same colour, the graph is not bipartite.
Time: O(V + E)   Space: O(V)
"""
from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        for start in range(len(graph)):
            if color[start] != -1:
                continue
            color[start] = 0
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if color[v] == -1:
                        color[v] = 1 - color[u]
                        queue.append(v)
                    elif color[v] == color[u]:
                        return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
    assert s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) is True
    assert s.isBipartite([[], [2], [1], []]) is True
    print("All tests passed")
