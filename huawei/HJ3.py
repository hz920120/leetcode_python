while True:
    try:
        n = int(input())
        data = []
        for i in range(n):
            data.append(int(input()))

        map = {}
        res = []
        for i, val in enumerate(data):
            if val not in map:
                res.append(val)
            map[val] = i
        res.sort()
        for v in res:
            print(v)
    except:
        break