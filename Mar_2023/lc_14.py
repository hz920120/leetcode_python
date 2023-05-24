import sys


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:

        def process(strs, res):
            if len(strs) == 1:
                return res + strs[0]
            s = strs.pop()
            if s == '':
                return res
            ch = s[0]
            stack = []
            if s[1:] != '' or not s[1:]:
                stack.append(s[1:])
            while strs:
                str = strs.pop()
                if str[0] != ch:
                    return res
                if s[1:] != '' or not s[1:]:
                    stack.append(str[1:])
            return process(stack, res + ch)

        return process(strs, '')

    def s1(self, strs: list) -> str:
        if not strs:
            return ''

        min_len = sys.maxsize
        for str in strs:
            min_len = min(min_len, len(str))

        p = 0
        res = ''
        while p < min_len:
            for i in range(len(strs)):
                if i == 0:
                    res += strs[i][p]
                    continue
                if i >0 and strs[i][p] != strs[i-1][p]:
                    return res[0:-1]

            p += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.s1(["flower",]))