"""
Experiment 9 (Trees) - Problem 2: Construct Binary Tree from Preorder and Inorder Traversal
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

Given the preorder and inorder traversal arrays of a binary tree, construct and
return the tree.

Approach: the first preorder element is the root. Its position in the inorder
array splits left and right subtrees. A hash map gives that position in O(1).
Time: O(n)   Space: O(n)
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {v: i for i, v in enumerate(inorder)}
        pre = iter(preorder)

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            root_val = next(pre)
            root = TreeNode(root_val)
            mid = index[root_val]
            root.left = build(lo, mid - 1)    # left first, matching preorder
            root.right = build(mid + 1, hi)
            return root

        return build(0, len(inorder) - 1)


def preorder_of(root):
    return [root.val] + preorder_of(root.left) + preorder_of(root.right) if root else []


def inorder_of(root):
    return inorder_of(root.left) + [root.val] + inorder_of(root.right) if root else []


if __name__ == "__main__":
    s = Solution()
    pre, ino = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
    root = s.buildTree(pre, ino)
    assert preorder_of(root) == pre and inorder_of(root) == ino
    root = s.buildTree([-1], [-1])
    assert root.val == -1 and root.left is None and root.right is None
    print("All tests passed")
