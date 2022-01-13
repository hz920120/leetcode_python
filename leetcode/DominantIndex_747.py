from typing import List


# def sort(nums):
#     left = partition(nums[:int(len(nums)/2)])
#     right = partition(nums[int((len(nums)/2) + 1):])
#
#
# def partition(nums):
#     '''
#     :param nums:
#     :return: 1最大，2次大
#     '''
#     if len(nums) == 2:
#         return (nums[0], nums[1], 0, 2) if (nums[0] > nums[1]) else (nums[1], nums[0], 1, 2)
#
#     if len(nums) == 1:
#         return nums[0], -1, 0, 1
#
#     # big_1, big2 = nums[0], nums[0]
#     # index_1, index_2 = 0, 0
#     left1, left2, index_l, len_l = partition(nums[:int(len(nums)/2)])
#     right1, right2, index_r, len_r = partition(nums[int((len(nums)/2)):])
#     max1 = left1 if left1 > right1 else right1
#     max2 = left2 if left2 > right2 else right2
#
#     # if left2 == -1:
#     #     index = index_l if left1 > right1 else (index_r + 1)
#     # # elif right2 == -1:
#     # #     index = index_l if left1 > right1 else (index_r + 2)
#     # else:
#     #     index = index_l if left1 > right1 else (index_r + 2)
#
#     if left1 > right1:
#         index = index_l
#     else:
#         index = index_r + len_l
#
#     return max1, max2, index, len_l + len_r


# test = [101,2,3,4,5,99, 100]
# x1, x2, index, len = partition(test)
# print(x1, x2, index, len)

class Solution:
    def __len__(self):
        return len(self)

    def partition(self, nums):

        if nums.__len__() == 2:
            return (nums[0], nums[1], 0, 2) if (nums[0] > nums[1]) else (nums[1], nums[0], 1, 2)

        if nums.__len__() == 1:
            return nums[0], -1, 0, 1

        # big_1, big2 = nums[0], nums[0]
        # index_1, index_2 = 0, 0
        left1, left2, index_l, len_l = self.partition(nums[:int(nums.__len__()/2)])
        right1, right2, index_r, len_r = self.partition(nums[int((nums.__len__()/2)):])
        # max1 = max(left1, left2, right1, right2)
        max1 = max(left1, right1)
        max2 = max((left2 if left2 > right2 else right2), min(left1, right1))

        if left1 > right1:
            index = index_l
        else:
            index = index_r + len_l
        return max1, max2, index, len_l + len_r

    def dominantIndex(self, nums: List[int]) -> int:
        if nums.__len__() == 1:
            return 0

        x1, x2, index, len = self.partition(nums)
        if x2 * 2 <= x1:
            return index
        else:
            return -1


s = Solution()
print(s.dominantIndex([1,3,6,0]))