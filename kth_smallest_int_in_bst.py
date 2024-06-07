# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count_nodes(node):
            if not node: return 0
            return count_nodes(node.left) + count_nodes(node.right) + 1

        n_left = count_nodes(root.left)

        if k <= n_left:
            return self.kthSmallest(root.left, k)
        elif k == n_left + 1:
            return root.val
        else:
            return self.kthSmallest(root.right, k - n_left - 1)

