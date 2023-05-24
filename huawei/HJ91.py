while True:
    try:
        a, b = map(int, input().split())
        # n, m = a+1, b+1

        def process(x, y):
            if x == a and y == b:
                return 1
            if x > a or y > b:
                return 0
            return process(x+1, y) + process(x,y+1)
        res = process(0 ,0)
        print(res)
    except:
        break