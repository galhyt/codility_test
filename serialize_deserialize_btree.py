# Definition for a binary tree node.
import json


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: TreeNode) -> str:
        if not root:
            return "[]"
        output = [root.val]
        arr = [root]
        while arr:
            node = arr.pop(0)
            if node.left:
                arr.append(node.left)
            if node.right:
                arr.append(node.right)
            output += list(map(lambda c: c.val if c else None, [node.left, node.right]))

        while output[-1] is None:
            output.pop(-1)
        return json.dumps(output)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> TreeNode:
        arr = json.loads(data)
        root = TreeNode(arr[0])

        def build(i, node):
            l = 2 * i + 1
            if l < len(arr):
                if arr[l] is not None:
                    node.left = TreeNode(arr[l])
                    build(l, node.left)
            else:
                i = len(arr)-2
                while i < len(arr):
                    i += 1

                if i < len(arr):
                    l = i
                    if arr[l] is not None:
                        node.left = TreeNode(arr[l])
                        build(l, node.left)

            r = l + 1
            if r < len(arr):
                a.add(r)
                if arr[r] is not None:
                    node.right = TreeNode(arr[r])
                    build(r, node.right)

        build(0, root)
        return root


if __name__ == '__main__':
    # [1,2,3,null,null,4,5,6,7]
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    root.right.left, root.right.right = TreeNode(4), TreeNode(5)
    root.right.left.left, root.right.left.right = TreeNode(6), TreeNode(7)
    sol = Codec()
    data = sol.serialize(root)
    print(data)
    tree_root =sol.deserialize(data)
    pass