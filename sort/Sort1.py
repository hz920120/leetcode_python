import random
import sys


class Solution(object):
    # i=0开始遍历，最小的数与i=0处数字swap
    # i=1开始遍历，最小的数与i=1处数字swap
    # i=2开始遍历，最小的数与i=2处数字swap
    # 以此类推
    def selectionSort(self, nums):
        if not nums:
            return nums

        l = len(nums)
        for i in range(l):
            min_index = i
            for j in range(i+1, l):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]


    # i 与 i+1 比较，大的放右边，接着i+1与i+2比较，大的放右边，一遍下来，最大的数在数组最右边
    # 接着进行第二次遍历，这次遍历最大的数在数组最右边-1
    # 接着进行第三次遍历，这次遍历最大的数在数组最右边-2
    # 以此类推
    def bubbleSort(self, nums):
        if not nums:
            return nums

        l = len(nums)
        for i in reversed(range(l)):
            j = 0
            while j < i:
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                j += 1

        return nums


    # 0~0有序，0~1有序，0~2有序.......0~N-1有序
    # index=i，当前数字往左看，比自己大，swap，继续往左看，比自己大，swap
    # 直到左边没有数字，或左边数字不比自己大，停，从index=i+1开始继续往左比较
    # 以此类推
    def insertionSort(self, nums):
        if not nums:
            return nums

        l = len(nums)
        for i in range(l):
            for j in range(i, -1, -1):
                if (j - 1) >= 0 and nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
        return nums


    # 找到一个中点，左右按大小merge
    # 左侧右侧分别再找一个中点，左右按大小merge
    # 递归中止条件是L==R
    # merge过程需要借助一个list存储排好序的数，然后再copy进原list相应的位置
    # def mergeSort(self, nums):
