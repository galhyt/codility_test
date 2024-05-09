from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def remove_leaves_equalizer(tree1: TreeNode, tree2: TreeNode):
    def _bfs(root: TreeNode) -> List:
        arr = [root]
        tree_bfs = []
        while len(arr) > 0:
            node = arr.pop(0)
            tree_bfs.append(node)
            if node.left:
                arr.append(node.left)
            if node.right:
                arr.append(node.right)
        return tree_bfs

    tree1_bfs = _bfs(tree1)
    tree2_bfs = _bfs(tree2)

    # check that tree2 leaves included in tree1's
    tree1_leaves = [node.val for node in tree1_bfs[::-1] if not node.left and not node.right]
    tree2_leaves = [node.val for node in tree2_bfs[::-1] if not node.left and not node.right]
    if len(tree2_leaves) > len(tree1_leaves):
        return False
    i = 0
    for j in range(len(tree2_leaves)):
        while tree1_leaves[i] != tree2_leaves[j]:
            i += 1
            if i == len(tree1_leaves) and j < len(tree2_leaves):
                return False

    # check that other than leaves nodes equal
    n = len(tree1_leaves)
    tree1_nodes = [node.val for node in tree1_bfs[:-n]]
    n = len(tree2_leaves)
    tree2_nodes = [node.val for node in tree2_bfs[:-n]]

    return tree1_nodes == tree2_nodes


if __name__ == '__main__':
    """
              1                             1
        2           3               2               3
    4       5   6       7       4               6
    """
    tree1 = TreeNode(1,
                        TreeNode(2, TreeNode(4), TreeNode(5)),
                        TreeNode(3, TreeNode(6), TreeNode(7)))

    tree2 = TreeNode(1,
                        TreeNode(2, TreeNode(4)),
                        TreeNode(3, TreeNode(6)))

    res = remove_leaves_equalizer(tree1, tree2)
    print(res)