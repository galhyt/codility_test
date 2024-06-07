# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_max_vals = {}

        def get_min_max(node):
            if id(node) in min_max_vals:
                return min_max_vals[id(node)]

            min_left, max_left = get_min_max(node.left) if node.left else (2 ** 31, -2 ** 31)
            min_right, max_right = get_min_max(node.right) if node.right else (2 ** 31, -2 ** 31)

            max_val = max(node.val, max_left, max_right)
            min_val = min(node.val, min_left, min_right)
            min_max_vals[id(node)] = (min_val, max_val)
            return min_val, max_val

        if root.left:
            if not self.isValidBST(root.left):
                return False
            max_left = get_min_max(root.left)[1]
            if root.val <= max_left:
                return False

        if root.right:
            if not self.isValidBST(root.right):
                return False
            min_right = get_min_max(root.right)[0]
            if root.val >= min_right:
                return False

        return True
