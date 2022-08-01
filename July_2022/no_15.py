class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []

        for i, val in enumerate(nums):
            flag = False
            while i > 0 and val == nums[i - 1]:
                flag = True
                break
            if flag:
                continue
            left, right = i + 1, len(nums) - 1
            target = val * -1

            while left < right:
                l = nums[left]
                r = nums[right]
                li = []
                if l + r == target:
                    li.extend([val, l, r])
                    # if li not in res:
                    #     res.append(li)

                    res.append(li)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif l + r < target:
                    left += 1
                else:
                    right -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    list = [-1,0,1,2,-1,-4]
    print(s.threeSum(list))