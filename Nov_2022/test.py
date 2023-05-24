class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in map:
                index = map.get(other)
                return [i, index]
            map[num] = i

    def twoSum167(self, numbers, target):
        map = {}
        for i, num in enumerate(numbers):
            other = target - num
            if other in map:
                index = map.get(other)
                return [i+1, index+1] if index >= i else [index+1, i+1]
            map[num] = i

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        set = []
        def findRoot(root):
            if not root:
                return False
            target = k - root.val
            if target in set:
                return True
            set.append(root.val)
            return findRoot(root.left) or findRoot(root.right)
        return findRoot(root)