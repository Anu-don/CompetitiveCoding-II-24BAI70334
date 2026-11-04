"""
Beyond Syllabus (Disjoint Set Union) - Problem 3: Evaluate Division
Link: https://leetcode.com/problems/evaluate-division/

Given equations Ai / Bi = value and queries Cj / Dj, return the answer to each
query, or -1.0 if it cannot be determined (including undefined variables).

Approach: weighted union-find. parent[x] = (root, ratio) where ratio = x / root.
Two variables are comparable iff they share a root; then
x / y = ratio(x) / ratio(y).
Time: O((E + Q) * alpha)   Space: O(V)
"""
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        parent = {}   # node -> parent
        weight = {}   # node -> value of node / parent

        def find(x: str) -> str:
            if parent[x] != x:
                root = find(parent[x])
                weight[x] *= weight[parent[x]]  # compress: x / root
                parent[x] = root
            return parent[x]

        def union(a: str, b: str, val: float) -> None:  # a / b = val
            for v in (a, b):
                if v not in parent:
                    parent[v] = v
                    weight[v] = 1.0
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                weight[ra] = val * weight[b] / weight[a]

        for (a, b), v in zip(equations, values):
            union(a, b, v)

        res = []
        for a, b in queries:
            if a not in parent or b not in parent or find(a) != find(b):
                res.append(-1.0)
            else:
                res.append(weight[a] / weight[b])
        return res


if __name__ == "__main__":
    s = Solution()
    out = s.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                         [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
    assert all(abs(x - y) < 1e-5 for x, y in zip(out, [6.0, 0.5, -1.0, 1.0, -1.0]))
    out = s.calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [1.5, 2.5, 5.0],
                         [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]])
    assert all(abs(x - y) < 1e-5 for x, y in zip(out, [3.75, 0.4, 5.0, 0.2]))
    print("All tests passed")
