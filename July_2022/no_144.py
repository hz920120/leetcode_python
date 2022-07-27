from util.Tree import TreeNode

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(root):
            if root is None:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res