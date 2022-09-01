class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def search_island(i, j):
            if i >= m or j >= n or i < 0 or j < 0:
                return 0
            if visited[i][j] == 1:
                return 0
            if grid[i][j] == '0':
                return 0
            else:
                visited[i][j] = 1
                if search_island(i + 1, j):
                    visited[i+1][j] = 1
                if search_island(i - 1, j):
                    visited[i - 1][j] = 1
                if search_island(i, j + 1):
                    visited[i][j + 1] = 1
                if search_island(i, j - 1):
                    visited[i][j - 1] = 1
                return 1



        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return 1 if grid[0][0] == '1' else 0

        visited = [[0 for i in range(n)] for i in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    res += search_island(i, j)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
    print(res)