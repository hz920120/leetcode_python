
#
#
# @param s string字符串
# @return bool布尔型
#
m = {
    '(':')',
    '{':'}',
    '[':']'
}
class Solution:
    def isValid(self , s):
        # write code here

        stack = []
        for ch in s:
            if ch == ')' or ch == '}' or ch == ']':
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if m[left] != ch:
                    stack.append(left)
            else:
                stack.append(ch)
        # stack1 = []
        # stack2 = []
        # for ch in s:
        #     stack1.append(ch)
        #
        # while len(stack1) > 0:
        #     c = stack1.pop()
        #     if c == ')' or c == '}' or c == ']':
        #         left = stack2.pop()
        #         if m[left] != c:
        #             stack2.append(left)
        #     else:
        #         stack2.append(c)

        return len(stack) == 0


if __name__ == '__main__':
    str = '()'
    s = Solution()
    print(s.isValid(str))