
m = {
    'A': -1,
    'D': 1,
    'W': 1,
    'S': -1
}
while True:
    try:
        data = list(input().split(';'))

        dir = []
        step = []
        for i, val in enumerate(data):
            if len(val) <= 3:
                try:
                    s = int(val[1:3])
                    d = val[0]
                    if d in m:
                        dir.append(d)
                        step.append(s)
                except:
                    pass
        h = 0
        v = 0
        for i in range(len(dir)):
            if dir[i] == 'A' or dir[i] == 'D':
                h += m[dir[i]] * step[i]
            if dir[i] == 'W' or dir[i] == 'S':
                v += m[dir[i]] * step[i]
        print(h, ',', v, sep='')
    except:
        break