#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A string字符串
# @return int整型
#
class Solution:
    def getLongestPalindrome(self , A: str) -> int:
        # write code here
        def check_Palindrome(s1):
            return s1 == s1[::-1]

        res = 1
        l = len(A)
        for i in range(0, l, 1):
            cur = A[i]
            for j in range(i+1, l, 1):
                if check_Palindrome(cur + A[j]):
                    cur += A[j]
                    res = max(res, len(cur))
                else:
                    cur += A[j]
        return res


if __name__ == '__main__':
    s = Solution()
    st = "ababababaaaaaaaaaaab"
    print(s.getLongestPalindrome(st))


