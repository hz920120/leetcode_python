
# 牛客 or7
class Solution:
    def getSolution(self , n):
        '''
        汉诺塔问题，动态规划
        :param n:
        :return:
        '''
        def process(n, start, end, other, res):
            if n == 1:
                res.append('move from ' + start + ' to ' + end)
            else:
                # 上方 n - 1 个从start挪到other上
                process(n-1, start, other, end, res)
                res.append('move from ' + start + ' to ' + end)
                process(n-1, other, end, start, res)
                # 剩下一个从start挪到end上

        res = []
        process(n, 'left', 'right', 'mid', res)
        return res


if __name__ == '__main__':
    n = 2
    s = Solution()
    print(s.getSolution(2))