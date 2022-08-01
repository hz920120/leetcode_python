class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        return 'a' * n if n % 2 else 'a' * (n - 1) + 'b'