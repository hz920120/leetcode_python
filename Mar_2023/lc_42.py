import sys

class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0

        # find maximum and index
        # m = -sys.maxsize - 1
        m_index = 0
        for i in range(len(height)):
            if height[i] > height[m_index]:
                m_index = i

        res = 0
        # from 0 to m-1
        min_index = 0
        for i in range(1, m_index):
            if height[i] < height[min_index]:
                res += height[min_index] - height[i]
            else:
                min_index = i


        # from len - 1 to m+1
        min_index = len(height) - 1
        for i in range(len(height) - 2, m_index, -1):
            if height[i] < height[min_index]:
                res += height[min_index] - height[i]
            else:
                min_index = i

        return res