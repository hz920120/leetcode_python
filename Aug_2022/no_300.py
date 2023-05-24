
'''
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return 1
        visited = [0] * l

        def f(i, pre_index):
            if i == l - 1:
                if nums[i] > nums[pre_index]:
                    return 1
                else:
                    return 0

            if nums[i] > nums[pre_index]:
                if visited[i] != 0:
                    return visited[i]
                m = f(i+1, i) + 1
                n = f(i+1, pre_index)
                if m >= n:
                    visited[i] = m
                    return m
                else:
                    return n
            else:
                return f(i+1, pre_index)
        res = 1
        for i in range(l):
            if visited[i] != 0:
                res = visited[i] if visited[i] > res else res
            temp = f(i, i) + 1
            print(visited)
            if f(i, i) + 1 > res:
                res = temp

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLIS([0,1,0,3,2,3]
)
    print(res)