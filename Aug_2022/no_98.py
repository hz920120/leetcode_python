import sys

from util.Util import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #
    #     def isBST(root):
    #         pre = [-sys.maxsize - 1]
    #         def check(root):
    #             if not root:
    #                 return True
    #             is_left_bst = check(root.left)
    #             if not is_left_bst:
    #                 return False
    #
    #             if root.val <= pre[0]:
    #                 return False
    #             else:
    #                 pre[0] = root.val
    #             return check(root.right)
    #         return check(root)
    #     return isBST(root)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        #套路解法
        class ReturnType:
            def __init__(self, isBST, max_val, min_val):
                self.isBST = isBST
                self.max_val = max_val
                self.min_val = min_val

        def isBST(root):
            rt = process(root)
            return rt.isBST

        def process(root):
            if not root:
                return root

            left = process(root.left)
            right = process(root.right)
            if left and right:
                isBST = left.isBST and right.isBST and (root.val > left.max_val) and (root.val < right.min_val)
                max_val = right.max_val
                min_val = left.min_val
                rt = ReturnType(isBST, max_val, min_val)
                return rt
            elif left:
                isBST = left.isBST and (root.val > left.max_val)
                max_val = root.val
                min_val = left.min_val
                rt = ReturnType(isBST, max_val, min_val)
                return rt
            elif right:
                isBST = right.isBST and (root.val < right.min_val)
                max_val = right.max_val
                min_val = root.val
                rt = ReturnType(isBST, max_val, min_val)
                return rt
            else:
                rt = ReturnType(True, root.val, root.val)
                return rt

        return isBST(root)



if __name__ == '__main__':
    root5 = TreeNode(val=3)
    root6 = TreeNode(val=6)
    # root3 = TreeNode(val=4)
    # root4 = TreeNode(val=5)
    root1 = TreeNode(val=1)
    root2 = TreeNode(val=4, left=root5, right=root6)
    root = TreeNode(val=5, left=root1, right=root2)
    s = Solution()
    res = s.isValidBST(root)
    print(res)