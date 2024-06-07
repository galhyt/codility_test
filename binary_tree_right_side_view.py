# Definition for a binary tree node.
from functools import reduce
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        levels = [[root]]
        level = levels[-1]

        while level:
            level = reduce(lambda s, anc: s + [anc.left, anc.right], level, [])
            level = list(filter(lambda n: n, level))
            if level:
                levels.append(level)

        return [level[-1].val for level in levels]

if __name__ == '__main__':
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    sol = Solution()
    print(sol.rightSideView(root))
