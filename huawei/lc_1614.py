m = {
    '(':')',
    '{':'}',
    '[':']'
}

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        # stack = []
        all = ['(', ')', '{', '}', '[', ']']
        res = 0
        depth = 0
        for ch in s:
            if ch in m.values():
                res = max(res, depth)
                depth -= 1
            elif ch in all:
                depth += 1
            else:
                pass
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth('(1+(2*3)+((8)/4))+1'))