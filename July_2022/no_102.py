from util.Tree import TreeNode

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue, res = [root], []

        while queue:
            level = []
            for i in range(len(queue)):
                tmp = queue.pop(0)
                level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            res.append(level)

        return res