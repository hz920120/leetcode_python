import sys

from util.Util import TreeNode

class Solution(object):
    def preOrder(self, node):
        if not node:
            return node
        stack = [node]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res


    def inOrder(self, node):
        if not node:
            return node
        stack1 = [node]
        res = []
        while stack1:
            curr = stack1.pop()
            res.append(curr.val)
            if curr.right:
                stack1.append(curr.right)
            if curr.left:
                stack1.append(curr.left)
        return res[::-1]


    def postOrder1(self, root):
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

    def postOrder(self, node):
        if not node:
            return node
        stack = [node]
        already = set()
        res = []
        while stack:
            curr = stack.pop()
            if curr.left and (curr.left not in already):
                stack.append(curr)
                stack.append(curr.left)
                continue
            res.append(curr.val)
            already.add(curr)
            if curr.right:
                stack.append(curr.right)
        return res

    # 层序遍历
    def f(self, root):
        if not root:
            return root
        queue = [root]
        res = []
        while queue:
            list = []
            for i in range(len(queue)):
                node = queue.pop(0)
                list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list)
        return res

    # 反转链表
    def reverse(self, node):
        if not node:
            return node
        curr, pre = node, None
        while curr:
            curr.next, curr, pre = pre, curr.next, curr
        return pre

    # 选择排序
    # 找一遍最小的与i=0位置swap
    # 找第二遍最小的与i=1位置
    def selectionSort(self,nums):
        if not nums or (len(nums) == 1):
            return nums

        min_value = sys.maxsize
        min_index = -1
        for i in range(len(nums)):
            for m in range(i, len(nums)):
                if nums[m] < min_value:
                    min_index = m
                    min_value = nums[m]
            # swap
            if min_index > -1:
                nums[i], nums[min_index] = nums[min_index], nums[i]
                min_value = sys.maxsize
                min_index = -1

        return nums

    def bubbleSort(self, nums):
        if not nums or (len(nums) == 1):
            return nums

        for i in range(len(nums)):
            for j in range(len(nums)-1-i):
                if j+1 > len(nums)-1:
                    break
                # compare and swap
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums

    # pivot随机选取
    # 荷兰国旗问题：<区域（初始化index=-1），=区域（介于<和>区域之间），>区域（初始化index=len(nums)）
    # 小于pivot：nums[i]与<区域的下一个位置swap，<区域右移一位，i++
    # 等于pivot：i++
    # 大于pivot：nums[i]与>区域的前一个位置swap，>区域左移一位
    # 终止条件，i >= >区域边界
    def quickSort(self, nums):
        if not nums or len(nums) < 2:
            return nums

        def qs(L, R):
            L, R, pointer = -1, len(nums), 0
            while pointer < R:
                if nums[pointer]

        def partition(L, R)




if __name__ == '__main__':
    # root5 = TreeNode(val=6)
    # root6 = TreeNode(val=7)
    # root3 = TreeNode(val=4)
    # root4 = TreeNode(val=5)
    # root1 = TreeNode(val=2, left=root3, right=root4)
    # root2 = TreeNode(val=3, left=root5, right=root6)
    # root = TreeNode(val=1, left=root1, right=root2)
    # s = Solution()
    # res = s.postOrder(root)
    # print(res)
    s =Solution()
    print(s.bubbleSort([5,1,1,2,0,0]))