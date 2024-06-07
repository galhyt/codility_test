# Definition for a binary tree node.
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_val = [-2**31]
        global good_nodes
        good_nodes = 0

        def dfs(node):
            global good_nodes
            if node.val >= max_val[-1]: good_nodes += 1
            max_val.append(max(max_val[-1], node.val))

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            max_val.pop(-1)

        dfs(root)
        return good_nodes


def print_tree(root):
    depth = math.log2(len(root))
    row_no = 2**depth

    for l in range(depth):
        no = 2**l
        margin = (row_no - no) // 2
        row = "".join(["    " for _ in margin])



if __name__ == '__main__':
    """
                                -1
                            
                    5                         -2
                        
            4               4           2           -2
            
                        -4          -2      3           -2
                        
                    0           -1        -3          -4    -3
                    
                  3                                         3   -3
                            
    """
    root = [-1, 5, -2, 4, 4, 2, -2, None, None, -4, None, -2, 3, None, -2, 0, None, -1, None, -3, None, -4, -3, 3, None,
            None, None, None, None, None, None, 3, -3]
    def dfs(idx):
        if idx >= len(root): return None
        if not root[idx]: return None

        node = TreeNode(root[idx])
        node.left = dfs(2*idx+1)
        node.right = dfs(2*idx+2)
        return node

    tree_root = TreeNode(-1, TreeNode(5, TreeNode(4),
                                      TreeNode(4, TreeNode(-4, TreeNode(0, TreeNode(3))))),
                         TreeNode(-2, TreeNode(2, TreeNode(-2, TreeNode(-1)), TreeNode(3, TreeNode(-3))),
                                  TreeNode(-2,None, TreeNode(-2, TreeNode(-4), TreeNode(-3, TreeNode(3), TreeNode(-3))))))
    sol =Solution()
    print(sol.goodNodes(tree_root))
