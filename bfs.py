

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root: TreeNode):
    arr = [root]
    while arr:
        node = arr.pop(0)
        yield node.val
        for child in (node.left, node.right):
            if child:
                arr.append(child)


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
    arr = list(bfs(root))
    assert arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]
