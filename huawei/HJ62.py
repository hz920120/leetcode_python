while True:
    try:
        x = int(input())
        res = 0
        while x > 0:
            res += x & 1
            x >>= 1
        print(res)
    except:
        break