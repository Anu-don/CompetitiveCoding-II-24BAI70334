"""
Experiment 6 (Hashing) - Problem 2: Clone Graph
Link: https://leetcode.com/problems/clone-graph

Given a reference node in a connected undirected graph, return a deep copy
(clone) of the entire graph.

Approach: DFS with a hash map old_node -> new_node, which also acts as the
visited set and handles cycles.
Time: O(V + E)   Space: O(V)
"""
from typing import Optional


class Node:
    def __init__(self, val: int = 0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        copies = {}

        def dfs(cur: "Node") -> "Node":
            if cur in copies:
                return copies[cur]
            clone = Node(cur.val)
            copies[cur] = clone
            for nb in cur.neighbors:
                clone.neighbors.append(dfs(nb))
            return clone

        return dfs(node)


def build(adj_list):
    """Helper: build a graph from an adjacency list (1-indexed) and return node 1."""
    if not adj_list:
        return None
    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, nbs in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j - 1] for j in nbs]
    return nodes[0]


def to_adj(node):
    """Helper: convert a graph back to an adjacency list."""
    if node is None:
        return []
    seen, order, stack = {node}, [], [node]
    while stack:
        cur = stack.pop()
        order.append(cur)
        for nb in cur.neighbors:
            if nb not in seen:
                seen.add(nb)
                stack.append(nb)
    order.sort(key=lambda x: x.val)
    return [[nb.val for nb in n.neighbors] for n in order]


if __name__ == "__main__":
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original = build(adj)
    copy = Solution().cloneGraph(original)
    assert to_adj(copy) == adj
    assert copy is not original and copy.neighbors[0] is not original.neighbors[0]
    assert Solution().cloneGraph(None) is None
    print("All tests passed")
