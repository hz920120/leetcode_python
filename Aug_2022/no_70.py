class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n为剩余台阶数
        def f_ori(n):
            if n == 0 or n == 1:
                return 1

            res = 0
            # 从当前台阶走一步
            res += f_ori(n-1)
            # 从当前台阶走两步
            res += f_ori(n-2)
            return res

        return f_ori(n)

    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # n为剩余台阶数
        def f_ori(n):
            if n == 0 or n == 1:
                return 1

            dp = []
            dp.append(1)
            dp.append(1)
            for i in range(2, n+1):
                dp.append(dp[i-1] + dp[i-2])
            return dp[n]

        return f_ori(n)

if __name__ == '__main__':
    s = Solution()
    # print(s.climbStairs1(4))

    # 对数器
    for i in range(40):
        s1 = s.climbStairs(i)
        s2 = s.climbStairs1(i)
        if s1 == s2:
            print('success')
        else:
            print('error')