# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_of_left_leaves(node, is_left=False):
            if not node.left and not node.right and is_left:
                return node.val
            s = 0
            if node.left:
                s += sum_of_left_leaves(node.left, True)
            if node.right:
                s += sum_of_left_leaves(node.right)
            return s

        return sum_of_left_leaves(root)


if __name__ == '__main__':
    # [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    sol = Solution()
    print(sol.sumOfLeftLeaves(root))
