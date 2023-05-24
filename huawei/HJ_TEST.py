while True:
    try:
        n = int(input())
        if n == 0:
            break

        res = 0
        while n >= 3:
            res += n // 3
            n = (n // 3) + (n % 3)
        if n == 2:
            res += 1
        print(res)

    except:
        break