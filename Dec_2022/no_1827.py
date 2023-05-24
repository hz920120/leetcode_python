class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        total = 0
        for index in range(1, len(nums)):
            if nums[index] <= nums[index-1]:
                total += nums[index-1] - nums[index] + 1
                nums[index] = nums[index-1] + 1

        return total


if __name__ == '__main__':
    s = Solution()
    t = s.minOperations([8])
    print(t)