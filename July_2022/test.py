import random

from util.Util import TreeNode

class Solution(object):
    def mergeSort(self, nums: list):
        def process(L, R):
            if L <= R:
                if L == R:
                    return nums[L:R+1]
                mid = L + ((R - L) >> 1)
                left = process(L, mid)
                right = process(mid+1, R)
                return merge(left, right)

        def merge(left, right):
            lp, rp = 0, 0
            res = []
            while lp < len(left) or rp < len(right):
                if lp >= len(left):
                    res.extend(right[rp:])
                    break

                if rp >= len(right):
                    res.extend(left[lp:])
                    break

                if left[lp] < right[rp]:
                    res.append(left[lp])
                    lp += 1
                elif left[lp] == right[rp]:
                    res.append(left[lp])
                    res.append(right[rp])
                    lp += 1
                    rp += 1
                else:
                    res.append(right[rp])
                    rp += 1
            return res
        return process(0, len(nums)-1)


    def quickSort(self, nums: list):
        def quickSort(L, R):
            if L < R:
                pivot_index = random.randint(L, R)
                nums[pivot_index], nums[R] = nums[R], nums[pivot_index]
                left, right = partition(L, R, nums)
                quickSort(L, left)
                quickSort(right, R)

        def partition(L, R, nums):
            pivot = nums[R]
            less, more = L - 1, R + 1
            while L < more:
                if nums[L] > pivot:
                    nums[more - 1], nums[L] = nums[L], nums[more - 1]
                    more -= 1
                elif nums[L] == pivot:
                    L += 1
                else:
                    nums[less + 1], nums[L] = nums[L], nums[less + 1]
                    less += 1
                    L += 1
            return less, more

        quickSort(0, len(nums) - 1)
        return nums

    def heapSort(self, nums):
        def heapInsert(nums, heapSize):
            father = max(0, (heapSize-1) // 2)
            while nums[heapSize] > nums[father]:
                nums[heapSize], nums[father] = nums[father], nums[heapSize]
                heapSize = father
                father = max(0, (heapSize-1) // 2)

        def heapify(nums, index, heapSize):
            while 2 * index + 1 < heapSize:
                largest = 2 * index + 2 if (2 * index + 2) < heapSize and nums[2 * index + 2] > nums[2 * index + 1] else 2 * index + 1
                largest = largest if nums[largest] > nums[index] else index
                if largest == index:
                    break
                nums[index], nums[largest] = nums[largest], nums[index]
                index = largest

        for i in range(len(nums) - 1, -1, -1):
            heapify(nums, i, len(nums))

        hs = len(nums)
        while hs > 0:
            nums[0], nums[hs - 1] = nums[hs - 1], nums[0]
            hs -= 1
            heapify(nums, 0, hs)
        return nums

    def s1(self, prices):
        '''
        终端某合作经销商遇到一个烦恼，由于下半年各平台的打折活动频繁，其终端商品价格具有一定波动性。
        经销商为了保证获取最大利益，将该商品在连续的K天内的价格记录在了数组prices中。
        经销商在某天（设为i）决定购入某商品，将它们存入仓库。并在另外一天（设为j），经销商将商品卖出（i <= j），
        同时他还需要付给该仓库j - i元的租金（每天租金为1）。此经销商请你帮忙判断一下基无现在的规则，
        最多可以赚多少利润，并输出。注：为了简化实现，整个过程只买卖一次。。
        '''
        dp = [0] * len(prices)
        min_val = prices[0]
        min_index = 0
        for index, val in enumerate(prices[1:]):
            if val < min_val:
                min_val = val
                min_index = index + 1
            dp[index+1] = max(dp[index], val - min_val - (index+1-min_index))
        return dp[-1]

    def s2(self, price):
        ret = 0
        minval = price[0]
        for i in range(len(price)):
            if price[i] - i <= minval:
                minval = price[i] - i
            else:
                ret = max(ret, price[i] - minval - i)

        return ret

    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []

        temp = set()
        for val in nums:
            temp.add(val)

        temp = list(temp)

        res = []
        for i in range(len(temp)):
            target = temp[i] * -1
            m = set()
            ans = [temp[i]]
            for j, val in enumerate(temp):
                if j == i:
                    continue
                other = target - val
                if other in m:
                    ans.extend([other, val])
                    ans.sort()
                    if ans not in res:
                        res.append(ans)
                m.add(val)
                ans = [temp[i]]
        return res

    def threeSum1(self, nums):
        if not nums:
            return []

        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            lp, rp = i + 1, len(nums) - 1
            while lp < rp:
                target = nums[i] + nums[lp] + nums[rp]
                if target == 0:
                    res.append([nums[i], nums[lp], nums[rp]])
                    lp += 1
                    rp -= 1
                    while lp < rp and nums[lp] == nums[lp - 1]:
                        lp += 1
                    while lp < rp and nums[rp] == nums[rp + 1]:
                        rp -= 1
                elif target < 0:
                    lp += 1
                else:
                    rp -= 1
        return res

    def trap(self, height: list) -> int:
        if not height:
            return 0

        # find a maximum value
        max_index = 0
        max_val = height[0]
        for i,val in enumerate(height):
            if val > max_val:
                max_val = val
                max_index = i

        left, right = 0, len(height) - 1
        res = 0
        for i in range(1, max_index, 1):
            if height[i] < height[left]:
                res += height[left] - height[i]
            else:
                left = i

        for i in range(right - 1, max_index, -1):
            if height[i] < height[right]:
                res += height[right] - height[i]
            else:
                right = i

        return res



if __name__ == '__main__':
    s = Solution()
    # nums1 = [random.randint(0, 10)  for x in range(10)]
    nums = [0,0,0,0]
    print(s.threeSum1(nums))