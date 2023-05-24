class Solution:
    def generateParenthesis(self, n: int):
        res = []
        def dfs(left, right, str):
            if left == 0 and right == 0:
                res.append(str)
                return

            if left > 0:
                dfs(left - 1, right, str + '(')

            if right > left:
                dfs(left, right - 1, str + ')')

        dfs(n, n, '')
        return res


if __name__ == '__main__':
    s = Solution()
    n = s.generateParenthesis(5)
    print(n)
    print(len(n))