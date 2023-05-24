# while True:
#     try:
#         n, k, x = map(int, input().split())
#         price_list = list(map(int, input().split()))
#         price_list.sort()
#
#         index = -1
#         for i, p in enumerate(price_list):
#             if p >= x:
#                 index = i
#                 break
#         # if x < price_list[0]:
#         #     index = -1
#
#         # 1:右边，0：左边
#         tag = 0
#         if index == -1 and price_list[-1]<x:
#             tag = 1
#
#         res = []
#         if index != -1:
#
#             mid = k // 2
#             for i in range(index - mid, index + mid + 1, 1):
#                 if i >= 0 and i <= len(price_list) - 1:
#                     if len(res) < k:
#                         res.append(price_list[i])
#         else:
#             if tag:
#                 res = price_list[len(price_list) - k - 1: len(price_list)]
#             else:
#                 res = price_list[0:k+1]
#         for i in res[:-1]:
#             print(i, end=' ')
#         print(res[-1])
#
#
#
#     except:
#         break







# 10 4 4
# 10 9 8 8 8 8 8 8 8 5

shufang = 1.715
ciwo = 1.7
zhuwo = 1.69 * 2
tatami = 1.7
a = (shufang + ciwo + zhuwo + tatami)*200
print('隐形: {}'.format(a))

yangtai = 2.396 * 1.12
b = yangtai * 230
print('阳台: {}'.format(b))
chufang = 1.36 * 0.73
c = chufang * 180
print('厨房: {}'.format(c))
cesuo1 = 1 if 0.735 * 1.303 < 1 else 0.735 * 1.303
cesuo2 = 1 if 1.315 * 0.725 < 1 else 1.315 * 0.725
d = (cesuo1+cesuo2) * 400
print('厕所: {}'.format(d))
print(a+b+c+d)