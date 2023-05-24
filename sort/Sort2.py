import sys
import random

class Solution:
    def selectionSort(self, nums):
        def swap(index1, index2, nums):
            nums[index1], nums[index2] = nums[index2], nums[index1]

        if not nums:
            return nums

        l = len(nums)
        min = sys.maxsize
        min_index = 0
        for i in range(l):
            for j in range(i, l):
                if nums[j] < min:
                    min = nums[j]
                    min_index = j
            swap(i, min_index, nums)
            min = sys.maxsize
            min_index = i
        return nums


    def bubbleSort(self, nums):
        if not nums:
            return nums

        l = len(nums)
        for i in range(l - 1):
            for j in range(l - 1 - i):
                nums[j], nums[j+1] = (nums[j], nums[j+1]) if nums[j+1] >= nums[j] else (nums[j+1], nums[j])
        return nums

    def insertionSort(self, nums):
        if not nums:
            return nums

        l = len(nums)
        for i in range(l):
            j = i
            while j >= 1:
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    j -= 1
                else:
                    break

        return nums


    def mergeSort(self, nums):
        def process(L, R, nums):
            if L == R:
                return nums[L:R+1]
            mid = L + ((R-L) >> 1)
            l_nums = process(L, mid, nums)
            r_nums = process(mid+1, R, nums)
            return merge(l_nums, r_nums)

        def merge(l_nums, r_nums):
            l_p, r_p = 0, 0
            res = []
            while l_p < len(l_nums) or r_p < len(r_nums):
                if l_p == len(l_nums):
                    res.extend(r_nums[r_p:])
                    break

                if r_p == len(r_nums):
                    res.extend(l_nums[l_p:])
                    break

                if l_nums[l_p] < r_nums[r_p]:
                    res.append(l_nums[l_p])
                    l_p += 1
                elif l_nums[l_p] == r_nums[r_p]:
                    res.append(l_nums[l_p])
                    res.append(r_nums[r_p])
                    l_p += 1
                    r_p += 1
                else:
                    res.append(r_nums[r_p])
                    r_p += 1
            return res


        if not nums:
            return nums

        return process(0, len(nums) - 1, nums)


    def quickSort3(self, nums):
        def quickSort(L, R, nums):
            if L < R:
                pivot_index = random.randint(L, R)
                nums[R], nums[pivot_index] = nums[pivot_index], nums[R]
                left, right = partition(L, R, nums)
                quickSort(L, left-1, nums)
                quickSort(right, R, nums)


        def partition(L, R, nums):
            pivot = nums[R]
            less = L-1
            more = R+1
            while L < more:
                if nums[L] < pivot:
                    nums[L], nums[less + 1] = nums[less + 1], nums[L]
                    L += 1
                    less += 1
                elif nums[L] == pivot:
                    L += 1
                else:
                    nums[L], nums[more - 1] = nums[more - 1], nums[L]
                    more -= 1
            return less+1, more


        quickSort(0, len(nums) - 1, nums)
        return nums

    def heapSort(self, nums):
        def heap_insert(nums, heap_size):
            # insert = (heap_size-1) if (heap_size-1) >= 0 else 0
            father = (heap_size-1) // 2 if (heap_size-1) // 2 >= 0 else 0
            while nums[heap_size] > nums[father]:
                # 向上移动
                nums[heap_size], nums[father] = nums[father], nums[heap_size]
                heap_size = father
                father = (heap_size - 1) // 2 if (heap_size - 1) // 2 >= 0 else 0

        def heapify(nums, index, heap_size):
            while 2 * index + 1 < heap_size:
                largest_index = 2 * index + 2 if (2 * index + 2) < heap_size and \
                                                 nums[2 * index + 2] > nums[2 * index + 1] else 2 * index + 1
                largest_index = largest_index if nums[largest_index] > nums[index] else index
                if largest_index == index:
                    break
                nums[index], nums[largest_index] = nums[largest_index], nums[index]
                index = largest_index

        for i in range(len(nums)-1, -1, -1):
            heapify(nums, i, len(nums))

        hs = len(nums)
        while hs > 0:
            nums[0], nums[hs - 1] = nums[hs - 1], nums[0]
            heapify(nums, 0, hs-1)
            hs -= 1
        return nums


    def heapSort1(self, nums):
        def heap_insert(nums, heap_size):
            # 往上走，比自己父大，就swap
            father = (heap_size - 1) // 2 if (heap_size - 1) // 2 >= 0 else 0
            while nums[heap_size] > nums[father]:
                nums[heap_size], nums[father] = nums[father], nums[heap_size]
                heap_size = father
                father = (heap_size - 1) // 2 if (heap_size - 1) // 2 >= 0 else 0




        def heapify(nums, index, heap_size):
            # 往下走，和孩子中较大的比较，如果还大，swap

            while 2 * index + 1 < heap_size:
                largest = 2 * index + 2 if (2 * index + 2 < heap_size and nums[2 * index + 2] > nums[2 * index + 1]) else 2 * index + 1
                largest = largest if nums[largest] > nums[index] else index
                if largest == index:
                    break
                nums[index], nums[largest] = nums[largest], nums[index]
                index = largest

        for i in range(len(nums)):
            heap_insert(nums, i)

        hs = len(nums)
        while hs > 0:
            nums[0], nums[hs - 1] = nums[hs - 1], nums[0]
            heapify(nums, 0, hs-1)
            hs -= 1
        return nums


# edge : from, to ,weight
# Node : val, in, out, nexts, edges
# graph : edge_list, node_list

if __name__ == '__main__':
    s = Solution()
    for i in range(100):
        nums = [random.randint(0, 20) for x in range(10)]
        b = nums.copy()
        a = s.heapSort1(nums)
        b.sort()
        if a != b:
            print('oops!')
            print(a)
            print(b)