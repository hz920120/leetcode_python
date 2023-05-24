while True:
    try:
        I = list(map(str, input().split()))
        R = list(map(int, input().split()))

        cnt_I = int(I[0])
        I_li = I[1:]

        cnt_R = R[0]
        R_li = R[1:]
        R_li.sort()
        R_li = [str(x) for x in R_li]

        res = {}
        already = set()
        total_cnt = 0
        for i in range(cnt_R):

            #key
            R_i = R_li[i]
            if R_i in already:
                continue
            #val [cnt, {val:index}]
            cnt = 0
            menu = []
            l = []
            for j in range(cnt_I):
                if len(I_li[j].split(R_i)) > 1:
                    cnt += 1
                    # [index:val]
                    menu.append(j)
                    menu.append(I_li[j])

            l.append(cnt)
            l.append(menu)
            already.add(R_i)
            if cnt > 0:
                total_cnt += cnt
                res[R_i] = l

        total_cnt += len(res)
        total_cnt *= 2
        print(total_cnt, end=' ')

        for k, v in res.items():
            print(k, end=' ')
            print(v[0], end=' ')
            for m in v[1]:
                print(m, end=' ')
    except:
        break


# a = '5'
# m = {'345':2, '456':5}
# l = [a]
# l.append(m)
# print(l)
