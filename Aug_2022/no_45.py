import sys


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # def f(i):
        #     if i == len(nums) - 1:
        #         return 0
        #     if i > len(nums) - 1 or nums[i] == 0:
        #         return sys.maxsize
        #     max_step = min(nums[i], len(nums) - 1 - i)
        #     left = sys.maxsize
        #     for m in range(1, max_step+1):
        #         left = min(left, f(i+m))
        #
        #     return left+1
        #
        # return f(0)
        l = len(nums)
        list = [0] * l

        def f1(i):
            if i == l-1:
                return 0
            if i > l-1 or nums[i] == 0:
                return sys.maxsize
            if list[i] > 0:
                return list[i]

            max_step = min(nums[i], len(nums) - 1 - i)
            left = sys.maxsize
            for m in range(1, max_step+1):
                left = min(left, f1(i+m))
            list[i] = left+1
            return left+1
        f1(0)
        return list[0]

    def jump1(self, nums):
        l = len(nums)
        if l == 1:
            return 0
        index = 0
        res = 0
        while index < l:
            if index + nums[index] >= l-1:
                return res + 1
            step = nums[index+1:index + nums[index]+1]
            for i in range(1, len(step) + 1):
                step[i-1] += i
            index += step.index(max(step)) + 1
            res += 1
        return res + 1

if __name__ == '__main__':
    nums = [2,4,1,5,6,7,3]
    s = Solution()
    print(s.jump(nums))

    # for i in range(1, 2):
    #     print(i)