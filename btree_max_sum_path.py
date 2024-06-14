from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right: return root.val

        if root.right and root.left:
            max_right = self.maxPathSum(root.right)
            max_left = self.maxPathSum(root.left)

            max_sum = max(max_left, max_right, max_right+root.val, max_left+root.val, max_right + max_left + root.val, root.val)
        elif root.right:
            max_right = self.maxPathSum(root.right)
            max_sum = max(max_right, max_right + root.val, root.val)
        else:
            max_left = self.maxPathSum(root.left)
            max_sum = max(max_left, max_left + root.val, root.val)

        return max_sum


if __name__ == '__main__':
    # [1, -2, -3, 1, 3, -2, null, -1]
    root = TreeNode(1,
                    TreeNode(-2, TreeNode(1, TreeNode(-1)), TreeNode(3)),
                    TreeNode(-3, TreeNode(-2)))
    sol = Solution()
    print(sol.maxPathSum(root))