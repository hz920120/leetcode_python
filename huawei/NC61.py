

while True:
    try:
        s = list(input().replace('[','').replace(']','').split(','))
        li, target = s[0:-1], int(s[-1])
        for i, str in enumerate(li):
            li[i] = int(str)

        map = {}
        for i in range(len(li)):
            tar = target - li[i]
            if tar in map:
                index = map[tar]
                print([index+1, i+1])
                break
            map[li[i]] = i
    except:
        break