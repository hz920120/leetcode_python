class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 1
        res = 0
        pre = nums[0]
        for val in nums[1:]:
            if val > pre:
                curr += 1
            else:
                res = max(curr, res)
                curr = 1
            pre = val
        return max(curr, res)

if __name__ == '__main__':
    s = Solution()
    n = [1,3,5,4,7,8,10]
    print(s.findLengthOfLCIS(n))