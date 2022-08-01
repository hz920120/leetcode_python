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

        return res
