from util.Util import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 一个节点，如果找到他的左节点和右节点有给定两个点的信息，
        # 直接返回当前节点；如果遇到其中一个节点，返回当前节点；
        # 左右都为空或者当前节点为空，直接返回空
        def LCA(root, p, q):
            if not root or root == p or root == q:
                return root

            left = LCA(root.left, p, q)
            right = LCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        def getLCA(root, p, q):
            if not root or root.val == p or root.val == q:
                return root

            left = getLCA(root.left, p, q)
            right = getLCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right

        return getLCA(root, p, q)

        return LCA(root, p, q)


if __name__ == '__main__':
    root7 = TreeNode(val=7)
    root4 = TreeNode(val=4)
    root2 = TreeNode(val=2, left=root7, right=root4)
    root6 = TreeNode(val=6)
    root5 = TreeNode(val=5, left=root6, right=root2)
    root0 = TreeNode(val=0)
    root8 = TreeNode(val=8)
    root1 = TreeNode(val=1, left=root0, right=root8)
    root3 = TreeNode(val=3, left=root5, right=root1)
    s = Solution()
    res = s.lowestCommonAncestor(root3, root5, root4)
    print(res)