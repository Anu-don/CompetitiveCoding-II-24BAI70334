"""
Experiment 9 (Trees) - Problem 1: Convert Sorted Array to Binary Search Tree
Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

Given a sorted integer array, convert it to a height-balanced binary search tree.

Approach: pick the middle element as root, recursively build the left and right
subtrees from the two halves.
Time: O(n)   Space: O(log n) recursion depth
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            return TreeNode(nums[mid], build(lo, mid - 1), build(mid + 1, hi))

        return build(0, len(nums) - 1)


def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def height(root):
    return 1 + max(height(root.left), height(root.right)) if root else 0


def is_balanced(root):
    if not root:
        return True
    return (abs(height(root.left) - height(root.right)) <= 1
            and is_balanced(root.left) and is_balanced(root.right))


if __name__ == "__main__":
    s = Solution()
    for arr in ([-10, -3, 0, 5, 9], [1, 3], [1], list(range(20))):
        root = s.sortedArrayToBST(arr)
        assert inorder(root) == arr   # still a valid BST (sorted inorder)
        assert is_balanced(root)      # height balanced
    assert s.sortedArrayToBST([]) is None
    print("All tests passed")
