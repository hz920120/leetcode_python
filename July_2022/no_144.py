from util.Tree import TreeNode

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # 简单递归
        # res = []
        # def dfs(root):
        #     if root is None:
        #         return
        #     res.append(root.val)
        #     dfs(root.left)
        #     dfs(root.right)
        #
        # dfs(root)
        # return res

        # 栈解法
        # if not root:
        #     return []
        # res, stack = [], [root]
        # while stack:
        #     curr = stack.pop()
        #     if curr:
        #         return
        #     res.append(curr.val)
        #     if curr.right:
        #         stack.append(curr.right)
        #     if curr.left:
        #         stack.append(curr.left)
        # return res

        # 模板解法
        if not root:
            return []

        curr, res, stack = root, [], []
        while curr or stack:
            while curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            tmp = stack.pop()
            curr = tmp.right

        return res