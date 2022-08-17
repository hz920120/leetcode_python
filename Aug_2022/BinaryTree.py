from util.Util import TreeNode

class Solution(object):
    def preOrder(self, root):
        #
        if not root:
            return root
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
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
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

if __name__ == '__main__':
    root5 = TreeNode(val=6)
    root6 = TreeNode(val=7)
    root3 = TreeNode(val=4)
    root4 = TreeNode(val=5)
    root1 = TreeNode(val=2, left=root3, right=root4)
    root2 = TreeNode(val=3, left=root5, right=root6)
    root = TreeNode(val=1, left=root1, right=root2)
    s = Solution()
    res = s.inOrder(root)
    print(res)