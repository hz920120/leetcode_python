while True:
    try:
        m = list(map(int, input().split()))

        def cal_water(x, y):
            res = 0
            value = min(m[x], m[y])
            for i in range(x, y+1):
                if m[i] < value:
                    res += value-m[i]
            return res

        def check(i, j):
            can = False
            water = 0
            left, right = i, i+1
            mini = i
            maxi = -1
            new = False
            while right <= j:
                if new:
                    left = right
                    right += 1
                    continue
                if m[mini] > m[right]:
                    if maxi != -1:
                        water += cal_water(left, right)
                        can = True
                        new = True
                        maxi = -1
                    else:
                        if m[right] < m[mini]:
                            mini = right
                            right += 1
                else:
                    if maxi == -1:
                        water += cal_water(left, right)
                        can = True
                        new = True
                        maxi = right
                    else:
                        maxi = right if m[right] > m[maxi] else maxi
                    right+=1

            return can, water


        n = len(m)
        res = 0
        max = 20000
        li = [-1, -1]
        for i in range(n):
            for j in range(i, n):
                can, water = check(i, j)
                if can:
                    if j-i < max and water > res:
                        li[0], li[1] = i, j
                        res = water

        if -1 in li:
            print(0)
        else:
            print('{} {}:{}'.format(li[0], li[1], res))
    except:
        break

# 9 6 2 5 4 9