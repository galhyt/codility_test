# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        def inorder_idx(val):
            for i in range(len(inorder)):
                if inorder[i] == val:
                    return i

        root = TreeNode(preorder[0])
        idx = inorder_idx(preorder[0])

        root.left = self.buildTree(preorder[1:idx+1], inorder[0:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root


if __name__ == '__main__':
    preorder = [1, 2, 3, 4]
    inorder = [2, 1, 3, 4]
    sol = Solution()
    root = sol.buildTree(preorder, inorder)
    pass