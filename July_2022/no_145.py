from util.Util import TreeNode

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        curr, res, stack = root, [], []
        while curr or stack:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.right
            tmp = stack.pop()
            curr = tmp.left

        return res[::-1]