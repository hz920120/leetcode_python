class Solution(object):
    def waysToChange(self, n):
        """
        :type n: int
        :rtype: int
        """
        value_list = [1, 5, 10, 25]
        l = [[0 for i in range(n+1)] for j in range(4)]
        l[0][0] = 1
        l[1][0] = 1
        l[2][0] = 1
        l[3][0] = 1
        if n >= 1:
            l[0][1] = 1
        if n >= 5:
            l[1][5] = 1
        if n >= 10:
            l[2][10] = 1
        if n >= 25:
            l[3][25] = 1

        def get_value(m, n):
            if m < 0 or m >= len(l) or n < 0 or n >= len(l[0]):
                return 0
            return l[m][n]

        for i in range(len(l) - 1, -1, -1):
            for j in range(len(l[0]) - 1):
                # 第i行 第j+1列
                l[i][j + 1] = get_value(i + 1, j + 1) + get_value(i, j + 1 - value_list[i])

        return (l[0][n]) % 1000000007


    def waysToChange2(self, n):
        """
        :type n: int
        :rtype: int
        """

        list = [1, 5, 10, 25]
        def f(index, left):
            # 金额越界，返回0
            if index > 3:
                return 0
            if left == 0:
                return 1
            # 面值比剩余金额大，返回0
            if left < list[index]:
                return 0
            # 剩余金额刚刚好等于当前面值，返回1，表示该次方案可行
            if left == list[index]:
                return 1
            res = 0
            res += f(index, left-list[index])
            res += f(index+1, left)
            return res
        return f(0, n) % 1000000007


if __name__ == '__main__':
    s= Solution()
    print(s.waysToChange2(20))


    value_list = [1, 5, 10, 25]

    for i in range(200):
        v1 = s.waysToChange(i)
        v2 = s.waysToChange2(i)
        if v1 == v2:
            print('success')
        else:
            print('error')
