while True:
    try:
        a, b = map(int, input().split())

        if a > b:
            a, b = b, a
        for i in range(b, b * a + 1, b):
            if i % a == 0:
                print(i)
                break
    except:
        break