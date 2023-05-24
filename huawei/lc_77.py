class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        res = []
        def dfs(left, right, curr: list):
            m = curr.copy()
            if len(curr) == k:
                res.append(curr)
                return
            for i in range(left, right + 1, 1):
                temp = m.copy()
                dfs(i+1, right, temp)
        dfs(1, n, res)
        return res




if __name__ == '__main__':
    s = Solution()
    print(s.combine(20, 16))
