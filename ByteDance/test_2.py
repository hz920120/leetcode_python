while True:
    try:
        building, dis = map(int, input().split())
        li = list(input().split())
        li = [int(x) for x in li]

        res = []
        for i1, point1 in enumerate(li):
            temp = set()
            li2 = li[i1+1:]
            for i2, point2 in enumerate(li2):
                if point2 - point1 > dis:
                    continue
                li3 = li2[i2+1:]
                for i3, point3 in enumerate(li3):
                    if point3 - point1 > dis:
                        continue
                    temp.add(point1)
                    temp.add(point2)
                    temp.add(point3)
                    if len(temp) > 0:
                        res.append(tuple(temp))
                        temp = set()
        # if len(res) == 0:
        #     print(0)
        # for i in res:
        #     print(i)
        print(len(res))
    except:
        break



'''
5 19
1 10 20 30 50


4 3
1 2 3 4

2 100
1 102
'''
