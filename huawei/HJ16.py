while True:
    try:
        N, m = map(int, input().split())
        goods = []
        for _ in range(m):
            goods.append(list(map(int, input().split())))

        # print(N, m, goods, sep=' ')

        already_main = [0] * m



        def process(k, money, num, already_main):
            if k >= m or money <= 0 or num == 0:
                return 0
            temp = already_main.copy()
            # 1. 要该商品
            v, p, q = goods[k]
            val1, val2 = 0, 0
            # 是从商品
            if q > 0:
                # 主商品买了吗
                if temp[q - 1]: # 买了, 直接买该从商品
                    if money >= v:
                        val1 = v * p
                        val1 += process(k+1, money - v, num - 1, temp)
                else: # 没买，先买主商品
                    v_m, p_m, q_m = goods[q - 1]
                    if money >= v_m:
                        val1 = v_m * p_m
                        temp2 = temp.copy()
                        temp2[q-1] = 1
                        if money - v_m >= v:# 买了主，钱还够，买从
                            val1 += v * p
                        val1 += process(k + 1, money - v_m - v, num - 1, temp2)
            else: #是主商品
                if money >= v:
                    val1 = v * p
                    temp2 = temp.copy()
                    temp2[k] = 1
                    val1 += process(k + 1, money - v, num - 1, temp2)
            # 2. 不要该商品
            val2 += process(k+1, money, num, temp)
            return max(val1, val2)

        x = process(0, N, m, already_main)
        print(x)
    except:
        break
        