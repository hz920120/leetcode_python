import random
import sys


class Solution(object):
    # i=0开始遍历，最小的数与i=0处数字swap
    # i=1开始遍历，最小的数与i=1处数字swap
    # i=2开始遍历，最小的数与i=2处数字swap
    # 以此类推
    def selectionSort(self, nums):
        if not nums or len(nums) == 1:
            return nums

        for i in range(len(nums)):
            min = sys.maxsize
            index_min = 0
            for j in range(i, len(nums)):
                if nums[j] < min:
                    min = nums[j]
                    index_min = j
            nums[i], nums[index_min] = nums[index_min], nums[i]
        return nums


    # i 与 i+1 比较，大的放右边，接着i+1与i+2比较，大的放右边，一遍下来，最大的数在数组最右边
    # 接着进行第二次遍历，这次遍历最大的数在数组最右边-1
    # 接着进行第三次遍历，这次遍历最大的数在数组最右边-2
    # 以此类推
    def bubbleSort(self, nums):
        if not nums or len(nums) == 1:
            return nums
        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                nums[j], nums[j+1] = (nums[j], nums[j+1]) if nums[j] <= nums[j+1] else (nums[j+1], nums[j])
        return nums

    # 0~0有序，0~1有序，0~2有序.......0~N-1有序
    # index=i，当前数字往左看，比自己大，swap，继续往左看，比自己大，swap
    # 直到左边没有数字，或左边数字不比自己大，停，从index=i+1开始继续往左比较
    # 以此类推
    def insertionSort(self, nums):
        if not nums or len(nums) == 1:
            return nums
        for i in range(len((nums))):
            for j in range(i, -1, -1):
                if ((j-1 >= 0) and nums[j - 1] > nums[j]):
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return nums


    # 二分：寻找局部最小值
    # return: index
    def regMin(self, nums):
        if not nums or (len(nums) == 1):
            return 0
        if nums[0] < nums[1]:
            return 0
        if nums[len(nums) - 1] < nums[len(nums) - 2]:
            return len(nums) - 1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if (nums[mid] < nums[mid - 1]) and (nums[mid] < nums[mid + 1]):
                return mid
            elif nums[mid] > nums[mid - 1]:
                right = mid
            else:
                left = mid

    # 找到一个中点，左右按大小merge
    # 左侧右侧分别再找一个中点，左右按大小merge
    # 递归中止条件是L==R
    # merge过程需要借助一个list存储排好序的数，然后再copy进原list相应的位置
    def mergeSort(self, nums):
        def process(L, R, nums):
            if L == R:
                res = []
                res.append(nums[L])
                return res
            mid = L + ((R - L) >> 1)
            left = process(L, mid, nums)
            right = process(mid+1, R, nums)
            return merge(L, mid, R, left, right, nums)


        def merge(L, M, R, left, right, nums):
            # L -> M, M+1 -> R, 两个区间都是从左往右移动不回退
            pointer_left, pointer_right = 0, 0
            helper = []
            while (pointer_left <= len(left) - 1) and (pointer_right <= len(right) - 1):
                if left[pointer_left] <= right[pointer_right]:
                    helper.append(left[pointer_left])
                    pointer_left += 1
                else:
                    helper.append(right[pointer_right])
                    pointer_right += 1
            # left 或者 right只有一个数组会越界，下面的while只会进一个
            while pointer_left <= len(left) - 1:
                helper.append(left[pointer_left])
                pointer_left += 1

            while pointer_right <= len(right) - 1:
                helper.append(right[pointer_right])
                pointer_right += 1

            return helper


        if not nums or len(nums) == 1:
            return nums

        return process(0, len(nums) - 1, nums)

    # pivot随机选取
    # 荷兰国旗问题：<区域（初始化index=-1），=区域（介于<和>区域之间），>区域（初始化index=len(nums)）
    # 小于pivot：nums[i]与<区域的下一个位置swap，<区域右移一位，i++
    # 等于pivot：i++
    # 大于pivot：nums[i]与>区域的前一个位置swap，>区域左移一位
    # 终止条件，i >= >区域边界
    def quickSort3(self, nums):
        def quickSort(L, R, nums):
            if L < R:
                # TODO select a pivot randomly, swap it with the last element
                pivot_index = random.choice(range(L, R+1))
                nums[pivot_index], nums[R] = nums[R], nums[pivot_index]
                # TODO find the borders of < region and > region
                left, right = partition(L, R, nums)
                # TODO L~(< region - 1) quick sort, (> region + 1)~R quick sort
                quickSort(L, left-1, nums)
                quickSort(right, R, nums)

        def partition(L, R, nums):
            pivot = nums[R]
            less = L - 1
            more = R + 1
            # L 代表当前数
            while L < more:
                if nums[L] < pivot:
                    nums[L], nums[less + 1] = nums[less + 1], nums[L]
                    less += 1
                    L += 1
                elif nums[L] == pivot:
                    L += 1
                else:
                    nums[L], nums[more - 1] = nums[more - 1], nums[L]
                    more -= 1
            return less + 1, more

        quickSort(0, len(nums) - 1, nums)
        return nums

    # heapify: 去掉头结点后如何保持大根堆（最后一个数放入头结点，然后和max(左节点,右节点)PK，子节点大，交换；不比任一子节点小，停止）
    # heap_insert: 插入一个数，如果比父节点大，和父节点交换，继续向上比较，直到不比父节点大或者已经上窜到根节点，停止
    # 一个节点的子节点: 2 * i + 1, 2 * i + 2
    # 一个节点的父节点: (i - 1) // 2 (注意i=0时该表达式的值与Java不一样，java=0, python=-1)
    def heapSort(self, nums):
        # 某个数处在heap的index位置，能否往下移动，限定heap size
        def heapify(heap, index, heap_size):
            left = index * 2 + 1
            # 如果有子节点
            while left < heap_size:
                # 找到子节点中最大的那个
                larger_index = left + 1 if (left + 1) < heap_size and (heap[left+1] > heap[left]) else left
                # 如果子节点大，交换
                if heap[larger_index] > heap[index]:
                    heap[larger_index], heap[index] = heap[index], heap[larger_index]
                else:
                    break
                index = larger_index
                left = larger_index * 2 + 1

        # 某个数处在heap的index位置，想要继续向上移动
        def heap_insert(heap, index):
            father = ((index - 1) // 2) if ((index - 1) // 2) >= 0 else 0
            while heap[index] > heap[father]:
                heap[index], heap[father] = heap[father], heap[index]
                index = father
                father = ((index - 1) // 2) if ((index - 1) // 2) >= 0 else 0


        # 先制作大根堆
        for i, val in enumerate(nums):
            heap_insert(nums, i)

        heap_size = len(nums) - 1
        nums[0], nums[heap_size] = nums[heap_size], nums[0]
        while heap_size > 0:
            heapify(nums, 0, heap_size)
            heap_size -= 1
            nums[0], nums[heap_size] = nums[heap_size], nums[0]

if __name__ == '__main__':
    # nums = [2,4,1,8,9]
    # s = Solution()
    # s.heapSort(nums)
    # print(nums)

    from queue import PriorityQueue
    heap = PriorityQueue()
    heap.put(1)
    heap.put(12)
    heap.put(3)
    heap.put(4)
    heap.put(4)
    heap.put(9)

    while not heap.empty():
        print(heap.get())
