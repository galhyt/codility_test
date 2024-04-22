from functools import reduce


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def prod(root: TreeNode):
    p_l = prod(root.left) if root.left else 1
    p_r = prod(root.right) if root.right else 1
    return p_l * p_r * root.val


def dfs(root: TreeNode):
    yield root.val
    if root.left: yield from dfs(root.left)
    if root.right: yield from dfs(root.right)


if __name__ == '__main__':
    tree = TreeNode(3, TreeNode(2),
                    TreeNode(1))
    print(prod(tree))
    # version 2
    for n in dfs(tree):
        print(n)
    print(reduce(lambda v, p: p*v, dfs(tree), 1))
