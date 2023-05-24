class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0

        is_Prime = [1] * n
        is_Prime[0] = 0
        is_Prime[1] = 0
        for i in range(2, int(n ** 0.5)  + 1):
            if is_Prime[i]:
                for j in range(i * i, n, i):
                    is_Prime[j] = 0

        return sum(is_Prime)















if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(3))

    # if n < 3:
    #     return 0
    #
    # is_Prime = [1] * (n)
    # is_Prime[0] = 0
    # is_Prime[1] = 0
    # for i in range(2, int(n ** 0.5) + 1, 1):
    #     if is_Prime[i]:
    #         for j in range(i * i, n, i):
    #             is_Prime[j] = 0
    # return sum(is_Prime)