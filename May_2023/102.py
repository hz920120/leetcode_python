# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from util.Util import TreeNode


# 二叉树的层序遍历
class Solution:
    def levelOrder(self, root):
        if not root:
            return root
        res = []
        queue = [root]
        while queue:
            li = []
            num = len(queue)
            for i in range(num):
                temp = queue.pop(0)
                li.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            res.append(li)
        return res

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return root

        res = []
        queue = [root]
        is_left = True
        while queue:
            num = len(queue)
            li = []
            for _ in range(num):
                temp = queue.pop(0)
                li.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            if is_left:
                res.append(li)
                is_left = False
            else:
                res.append(li[::-1])
                is_left = True
        return res

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 空节点返回null
        if not root:
            return None
        # 如果当前root的值为q或者q，那么返回当前节点
        if root.val == q.val or root.val == p.val:
            return root

        # 如果上边条件不满足，则从左边及右边去找
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        # 如果l、r都不为空，说明root为公共祖先
        if l and r:
            return root
        # 如果l、r有一个不为空，返回不为空的那个
        if l or r:
            return l if l else r
        # 如果l、r都为空，返回空
        if not l and not r:
            return None



if __name__ == '__main__':
    node1 = TreeNode(val=15)
    node2 = TreeNode(val=7)
    node3 = TreeNode(val=20, left=node1, right=node2)
    node4 = TreeNode(val=9)
    node5 = TreeNode(val=3, left=node4, right=node3)
    # node6 = TreeNode(val=3)
    # node7 = TreeNode(val=3)
    # node8 = TreeNode(val=3)
    s = Solution()
    print(s.zigzagLevelOrder(node5))