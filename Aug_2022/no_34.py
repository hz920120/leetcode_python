class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def search(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid - 1
                if nums[mid] < target:
                    left = mid + 1
            return left
        a = search(nums, target)
        b = search(nums, target + 1)
        if a == len(nums) or nums[a] != target:
            return [-1, -1]
        return [a, b-1]

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange(nums=[1,2,2], target=2))