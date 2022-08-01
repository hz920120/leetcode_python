class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 0:
            return ''
        even = False
        if n % 2 == 0:
            even = True
        res = '' if even else 'm'
        for i in range(n-1):
            if i == 0:
                res += 'x'
            elif i != 0:
                res += 'y'
        return res + 'y' if even else res