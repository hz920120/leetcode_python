from util.Util import TreeNode

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def getLCA(root):
            if not root:
                return None

            if root.val == p or root.val == q:
                return root

            left = getLCA(root.left)
            right = getLCA(root.right)
            if (not left) and (not right):
                return None
            if left and right:
                return root

            return left if not right else right

        return getLCA(root).val


if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(5)
    root = TreeNode(3, node2, node1)
    print(s.lowestCommonAncestor(root, 5, 1))