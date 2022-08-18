from util.Util import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        class ReturnType:
            def __init__(self, isBalance, height):
                self.isBalance = isBalance
                self.height = height

        def isValid(root):
            rt = process(root)
            return rt.isBalance

        def process(root):
            if not root:
                rt = ReturnType(True, 0)
                return rt

            left = process(root.left)
            right = process(root.right)
            isBalance = left.isBalance and right.isBalance and abs(left.height - right.height) < 2
            height = max(left.height, right.height) + 1
            rt = ReturnType(isBalance, height)
            return rt



        return isValid(root)