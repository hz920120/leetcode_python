class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 暴力
        # for i in range(len(nums)):
        #     # if nums[i] > target:
        #     #     continue
        #     other = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j] == other:
        #             return [i, j]

        # 哈希查找
        # map = {val: i for i, val in enumerate(nums)}
        #
        # for i, val in enumerate(nums):
        #     other = target - val
        #     if map.__contains__(other):
        #         index = map.get(other)
        #         if i != index:
        #             return [i, index]

        # 进一步优化：O(n)
        map = {}
        for i, val in enumerate(nums):
            other = target - val
            if other in map:
                index = map.get(other)
                return [i, index]
            map[val] = i




if __name__ == '__main__':
    s = Solution()
    p = s.twoSum(nums=[-1,-2,-3,-4,-5], target=-8)
    print(p)