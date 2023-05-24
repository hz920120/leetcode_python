while True:
    try:
        n, m = map(int, input().split())
        maze = []
        for _ in range(n):
            maze.append(list(map(int, input().split())))

        def dfs(x, y, res: list):
            if x == n-1 and y == m-1:
                res.append((x,y))
                return 1, res
            if x >= n or y >= m or maze[x][y] == 1:
                return 0, res
            res.append((x,y))
            tmp = res.copy()
            s1, list1 = dfs(x+1, y, tmp)
            tmp = res.copy()
            s2, list2 = dfs(x, y+1, tmp)
            if s1 == s2:
                if s1 == 1:
                    return s1, list1
                else:
                    return s1, res
            else:
                if s1 == 1:
                    return s1, list1
                else:
                    return s2, list2

        a, res = dfs(0,0,[])
        for i in res:
            print(str(i).replace(' ',''))

    except:
        break