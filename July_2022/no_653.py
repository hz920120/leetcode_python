from util.Util import TreeNode

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        # O(2N)算法
        # if not root:
        #     return False
        #
        # curr, res, stack = root, [], []
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     tmp = stack.pop()
        #     res.append(tmp.val)
        #     curr = tmp.right
        #
        # lp, rp = 0, len(res) - 1
        # while lp < rp:
        #     sum = res[lp] + res[rp]
        #     if sum == k:
        #         return True
        #     elif sum < k:
        #         lp += 1
        #     else:
        #         rp -= 1
        #
        # return False


        # 优化，哈希查找
        set = []
        def find(root):
            if not root:
                return False
            value = k - root.val
            if value in set:
                return True
            set.append(root.val)
            return find(root.left) or find(root.right)
        return find(root)

if __name__ == '__main__':
    root5 = TreeNode(val=7)
    root3 = TreeNode(val=2)
    root4 = TreeNode(val=4)
    root1 = TreeNode(val=3, left=root3, right=root4)
    root2 = TreeNode(val=6, right=root5)
    root = TreeNode(val=5, left=root1, right=root2)
    s = Solution()
    res = s.findTarget(root, 9)
    print(res)