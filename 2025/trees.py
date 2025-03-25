# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from util.Util import TreeNode


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 根 -> 左 -> 右
        if not root:
            return []

        res, stack = [], []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            root = tmp.right
        return res

    def postorder(self, root: Optional[TreeNode]) -> List[int]:
        #  左 -> 右 -> 根
        if not root:
            return []

        res = []
        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            tmp = stack.pop()
            root = tmp.left
        return res[::-1]

    def inorder(self, root: Optional[TreeNode]) -> List[int]:
        #  左 -> 根 -> 右
        if not root:
            return []

        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
        return res

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        res = []
        while queue:
            curr_res = []
            num = len(queue)
            for i in range(num):
                node = queue.pop()
                curr_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(curr_res)
        return res