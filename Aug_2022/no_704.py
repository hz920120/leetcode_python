class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            left += 1
            right -= 1
        return -1
