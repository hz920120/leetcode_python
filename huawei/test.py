import random

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # {val: index}
        m = {}
        for index, val in enumerate(nums):
            n = target - val
            if n in m.keys():
                return [m.get(n), index]
            m[val] = index

if __name__ == '__main__':
    # s = Solution()
    # # s.twoSum([2,7,11,15], 9)
    #
    # print(random.randint(0,3))
    #
    # random_list = [random.randint(0,100) for x in range(10)]
    # random_list.sort()
    # print(random_list, end=' ')
    #
    # i1 = random.randint(0,9)
    # i2 = random.randint(0,9)
    # target = random_list[i1] + random_list[i2]
    #
    #
    # print(target)
    #
    #
    # def vio(nums, target):
    #     for i, val1 in enumerate(nums):
    #         for j, val2 in enumerate(nums[i+1:]):
    #             if val1 + val2 == target:
    #                 return [i, i+1+j]
    # # print(vio(random_list, target) == s.twoSum(random_list, target))
    # for i in range(1000):
    #     a = vio(random_list, target)
    #     b = s.twoSum(random_list, target)
    #     if not a == b:
    #         print(random_list)
    #         print(target)
    #         print(a)
    #         print(b)
    #         break
    #     print('success', i, sep=' ')
    x = [random.randint(0,10) for x in range(20)]
    print(x)