from util.Util import TreeNode

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # 递归
        # res = []
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     res.append(root.val)
        #     inorder(root.right)
        #
        # inorder(root)
        # return res

        # 栈解法
        res = []
        if not root:
            return res
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                if tmp.right:
                    root = tmp.right

        return res

    def preOrder(self, root: TreeNode):
        res = []
        if not root:
            return res

        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            root = tmp.right
        return res

    def postOrder(self, root: TreeNode):
        res = []
        if not root:
            return res

        stack = []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            tmp = stack.pop()
            root = tmp.left
        return res[::-1]


    def pre(self, root):
        if not root:
            return []

        res = []
        stack = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            tmp = stack.pop()
            root = tmp.right
        return res

    def in1(self, root):
        if not root:
            return []

        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right

        return res


    def post(self, root):
        if not root:
            return []

        res, stack = [], []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            tmp = stack.pop()
            root = tmp.left

        return res[::-1]


























