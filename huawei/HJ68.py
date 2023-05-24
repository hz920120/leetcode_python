while True:
    try:
        n = int(input())
        tag = int(input())
        ori = []
        for _ in range(n):
            name, g = map(str, input().split())
            ori.append((name, int(g)))
        res = sorted(ori, key=lambda x: x[1], reverse=(not tag))
        for i, val in enumerate(res):
            print(val[0], ' ', val[1], sep='')
    except:
        break

# m = {}
# m['a'] = 1
# m['b'] = 2
# m['c'] = 3
# print(m)
# # f = lambda x: print(x[1])
# # f(m.items())
# # sorted(key=)
# for i in m.keys():
#
#     print(i)
#     print(m[i])

# 4
# 0
# peter     96
# jack      70
# Tom       70
# smith     67