

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def remove_leaves(root: TreeNode):
    def _add_to_stack(node: TreeNode):
        if not node:
            return
        stack.append(node)
        for child in [node.left, node.right]:
            _add_to_stack(child)

    stack = []
    _add_to_stack(root)

    remove_order = stack[-1::-1]
    return remove_order


if __name__ == '__main__':
    """
              1
        2           3
    4       5   6       7
    """
    root = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(5)),
                    TreeNode(3, TreeNode(6), TreeNode(7)))
    remove_order = remove_leaves(root)
    print([node.val for node in remove_order])
