while True:
    try:
        n = int(input())
        data = list(map(int, input().split()))
        tag = int(input())
        data.sort()
        if not tag:
            for i in range(len(data) - 1):
                print(str(data[i]), end=' ')
            print(str(data[-1]))
        else:
            for i in range(len(data) - 1, 0, -1):
                print(str(data[i]), end=' ')
            print(str(data[0]))

    except:
        break

