
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root: TreeNode, arr=[]):
    arr.append(root.val)
    if root.left: dfs(root.left, arr)
    if root.right: dfs(root.right, arr)
    return arr


def dfs_gen(root: TreeNode):
    yield root.val
    if root.left: yield from dfs_gen(root.left)
    if root.right: yield from dfs_gen(root.right)


if __name__ == '__main__':
    """
                    1
            2               3
        4       5
      6   7   8   9
    """
    root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6),
                                            TreeNode(7)),
                                TreeNode(5, TreeNode(8),
                                         TreeNode(9))),
                    TreeNode(3))
    arr = dfs(root)
    assert arr == [1, 2, 4, 6, 7, 5, 8, 9, 3]
    print(arr)
    print([v for v in dfs_gen(root)])
