class Solution:
    def trapRainWater(self, heightMap):
        def trans(heightMap):
            m = len(heightMap)
            n = len(heightMap[0])

            res = []
            for i in range(n):
                t_l = []
                for j in range(m):
                    t_l.append(heightMap[j][i])
                res.append(t_l)
            return res

        def trap(height):
            if not height:
                return 0

            # find maximum and index
            # m = -sys.maxsize - 1
            m_index = 0
            for i in range(len(height)):
                if height[i] > height[m_index]:
                    m_index = i

            res_li = [0] * len(height)
            # from 0 to m-1
            min_index = 0
            for i in range(1, m_index):
                if height[i] < height[min_index]:
                    res_li[i] = height[min_index] - height[i]
                else:
                    min_index = i

            # from len - 1 to m+1
            min_index = len(height) - 1
            for i in range(len(height) - 2, m_index, -1):
                if height[i] < height[min_index]:
                    res_li[i] = height[min_index] - height[i]
                else:
                    min_index = i

            return res_li

        m = len(heightMap)
        n = len(heightMap[0])
        map1 = []
        map2 = []

        heightMap_T = trans(heightMap)
        # hor
        for i in range(m-2):
            temp = trap(heightMap[i+1])
            map1.append(temp[1: -1])

        # ver
        for i in range(n-2):
            temp = trap(heightMap_T[i+1])
            map2.append(temp[1: -1])
        map2 = trans(map2)

        res = 0
        for i in range(len(map1)):
            for j in range(len(map1[0])):
                res += min(map1[i][j], map2[i][j])

        return res


if __name__ == '__main__':
    a = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]

    s = Solution()
    print(s.trapRainWater(a))