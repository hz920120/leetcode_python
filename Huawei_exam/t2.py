while True:
    try:
        m = list(map(int, input().split()))
        l = len(m)


        def cal(pre, count, index):
            return count - pre * index


        def process(pre, index):
            if index == l:
                return 0
            # 条数够了
            if pre + m[index] >= 100:
                return cal(pre, 100, index)

            #此刻不上报
            val2 = process(pre + m[index], index + 1)
            # 此刻上报
            val3 = cal(pre, pre + m[index], index)
            return max(val2, val3)

        print(process(0, 0))
    except:
        break