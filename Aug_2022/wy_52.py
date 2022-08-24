# 牛客 WY52

import sys

count = 0
weight = 0
snack_weight = []
lines = 2
break_count = 0
for line in sys.stdin:
    a = line.split()
    if break_count == 0:
        count = int(a[0])
        weight = int(a[1])
    if break_count == 1:
        for w in a:
            snack_weight.append(int(w))
    break_count += 1
    if break_count == lines:
        break

print(int(count))
print(int(weight))
print(snack_weight)


# 之前的i-1个零食已经放好，现在要决定 是否 放第i个重量为m的零食
def process(i, total_weight, snacks, amount, res):
    # i <= amount
    if i > amount:
        return 0
    # 超重
    if snacks[i] > (weight - total_weight):
        return 0
    if i == amount and snacks[i] + total_weight < weight:
        return 1

    # 不超重
    res += (process(i+1, total_weight+snacks[i], snacks, amount, res) + process(i+1, total_weight, snacks, amount, res))
    return res


res = 0
process(0, 0, snack_weight, count - 1, res)
print(res)
