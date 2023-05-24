while True:
    try:
        n = int(input())
        train_in = list(map(int, input().split()))
        res = set()

        def process(index, stack):
            if index == len(train_in):
                while len(stack) > 0:
                    res.add(stack)
                return
            # index位置进去直接出
            temp = stack.copy()
            temp.insert(0, train_in[index])
            process(index + 1, temp)
            temp = stack.copy()
            temp.append(train_in[index])
            process(index + 1, temp)
        process(0, [])
        print(res)


    except:
        break