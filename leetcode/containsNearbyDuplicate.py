class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for l in range(len(nums)):
            temp = nums[l]
            for ele in nums[l + 1:l + k + 1]:
                if temp == ele:
                    return True

        return False


s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1,2,3], 2))