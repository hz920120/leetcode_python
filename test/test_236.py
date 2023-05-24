from util.Util import TreeNode


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        '''
        一个节点，如果找到他的左节点和右节点有给定两个点的信息，直接返回当前节点；如果遇到其中一个节点，返回当前节点；左右都为空或者当前节点为空，直接返回空
        '''
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root
        elif l or r:
            return l if l else r
        else:
            return None

if __name__ == '__main__':
    s = Solution()
    node1 = TreeNode(1)
    node2 = TreeNode(5)
    root = TreeNode(3, node2, node1)
    print(s.lowestCommonAncestor(root, node2, node1))