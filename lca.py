# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        vp, vq = p.val, q.val
        arr = [root]
        tree_arr = []
        while arr:
            node = arr.pop(0)
            tree_arr.append(node)
            if node:
                if node.val == vq:
                    iq = len(tree_arr) - 1
                if node.val == vp:
                    ip = len(tree_arr) - 1

                arr.append(node.left)
                arr.append(node.right)

        while not tree_arr[-1]:
            tree_arr.pop(-1)

        # ancestors of p
        pindices = []
        iap = ip
        while iap >= 0:
            pindices.append(iap)
            iap = (iap - (2 if iap % 2 == 0 else 1)) // 2

        qindices = []
        iaq = iq
        while iaq >= 0:
            qindices.append(iaq)
            iaq = (iaq - (2 if iaq % 2 == 0 else 1)) // 2

        i, j = 0, 0
        while qindices and pindices:
            iq, ip = qindices[i], pindices[j]
            if iq == ip:
                return tree_arr[iq]
            elif iq > ip:
                i += 1
            else:
                j += 1


if __name__ == '__main__':
    # [3,5,1,6,2,0,8,null,null,7,4]
    root = TreeNode(3,
                    TreeNode(5, TreeNode(6), TreeNode(2,
                                                      TreeNode(7), TreeNode(4))),
                    TreeNode(1, TreeNode(0), TreeNode(8)))
    # [37,-34,-48,null,-100,-101,48,null,null,null,null,-54,null,-71,-22,null,null,null,8]
    root = TreeNode(37,
                    TreeNode(-34, TreeNode(None), TreeNode(-100)),
                    TreeNode(-48, TreeNode(-101, TreeNode(-54)),
                             TreeNode(48, TreeNode(-71), TreeNode(-22))))
    sol = Solution()
    lca = sol.lowestCommonAncestor(root, root.left, root.left.right.right)
    print(lca.val)