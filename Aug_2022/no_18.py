class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            flag1 = False
            while i > 0 and nums[i] == nums[i - 1]:
                flag1 = True
                break
            if flag1:
                continue
            n1 = nums[i]
            for j in range(i + 1, len(nums) - 2):
                flag2 = False
                while j > i and nums[j] == nums[j - 1]:
                    flag2 = True
                    break
                if flag2:
                    continue
                n2 = nums[j]
                left, right = j + 1, len(nums) - 1
                val = target - n1 - n2
                while left < right:
                    l = nums[left]
                    r = nums[right]
                    list = []
                    if l + r == val:
                        list.extend([n1, n2, l, r])
                        res.append(list)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif l + r < val:
                        left += 1
                    else:
                        right -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    list = [-2,-1,-1,1,1,2,2]
    print(s.fourSum(list, 0))