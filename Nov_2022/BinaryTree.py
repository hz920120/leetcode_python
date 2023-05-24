from util.Util import TreeNode

class Solution(object):
    def preOrder(self, root):
        if not root:
            return root

        stack = [root]
        res = []
        if stack:
            node = stack.pop()
            res.append(node.val)
            if not node.right:
                stack.append(node.right)
            if not node.left:
                stack.append(node.left)
        return res


    def postOrder(self, root):
        if not root:
            return root

        stack1 = [root]
        stack2 = []
        res = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        while stack2:
            node = stack2.pop()
            res.append(node.val)
        return res

    def inOrder(self, root):
        if not root:
            return root

        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                res.append(node.val)
                root = node.right

        return res

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root

        queue = [root]
        res = []
        while queue:
            num = len(queue)
            list = []
            for i in range(num):
                curr = queue.pop(0)
                list.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(list)
        return res

