class Solution(object):
    def __init__(self):
        self.alive = 0
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid:
            return 0
        # 0
        empty = 0
        # 1

        # 2
        dead = 0

        m = len(grid)
        n = len(grid[0])

        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty += 1
                elif grid[i][j] == 1:
                    self.alive += 1
                else:
                    tmp = [i, j]
                    stack.append(tmp)
                    dead += 1

        if dead == 0 and self.alive > 0:
            return -1

        if self.alive == 0:
            return 0


        def change(x, y, stack):
            if x < 0 or y < 0 or x >= m or y >= n:
                return
            if grid[x][y] != 1:
                return
            grid[x][y] = 2
            self.alive -= 1
            stack.append([x, y])

        minute = 0
        while len(stack) > 0:
            for _ in range(len(stack)):
                p = stack.pop(0)
                i, j = p[0], p[1]
                if grid[i][j] == 2:
                    # 遍历上下左右
                    change(i, j + 1, stack)
                    change(i, j - 1, stack)
                    change(i - 1, j, stack)
                    change(i + 1, j, stack)
            minute += 1
        if self.alive > 0:
            return -1
        else:
            return minute-1





if __name__ == '__main__':
    s  =Solution()
    grid = [[2],[1]]
    print(s.orangesRotting(grid))