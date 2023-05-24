# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util.Util import TreeNode
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res

        stack = [root]
        while len(stack) > 0:
            l = len(stack)
            li = []
            for i in range(l):
                curr = stack.pop(0)
                li.append(curr.val)
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)
            res.append(li)
        return res

if __name__ == '__main__':
    root = None
    s = Solution()
    s.levelOrder()