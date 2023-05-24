while True:
    try:
        n = int(input())
        m = {}
        for _ in range(n):
            index, val = map(int, input().split())
            if index in m:
                m[index] += val
            else:
                m[index] = val

        for k in sorted(m):
            print(k,' ',m[k], sep='')
    except:
        break