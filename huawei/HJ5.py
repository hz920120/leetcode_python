'''
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
'''
map = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}
while True:
    try:
        hex = input()
        hex = hex.replace('0x', '')
        li = [*hex]
        length = len(li)
        i = length - 1
        res = 0
        for d in li:
            n = map[d]
            res += n * (16**i)
            i-=1
        print(res)
    except:
        break