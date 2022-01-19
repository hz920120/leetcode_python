class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        s = []
        for index in range(len(nums)):
            if len(s) > k:
                s.pop()
            if nums[index] in s:
                return True
            s.append(nums[index])
        return False


s = Solution()
print(s.containsNearbyDuplicate([4,1,2,3,1,5], 3))