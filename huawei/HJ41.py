while True:
    try:
        n = int(input())
        wt_li = list(map(int, input().split()))
        ct_li = list(map(int, input().split()))

        s = set()
        s.add(0)
        for i in range(n):
            cur_li = []
            for j in range(1, ct_li[i]+1, 1):
                cur_li.append(wt_li[i] * j)
            tmp = set()
            for m in s:
                for j in cur_li:
                    tmp.add(m + j)
            s |= tmp
        print(s)
        print(len(s))
    except:
        break

