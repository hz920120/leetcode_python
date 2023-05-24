while True:
    try:
        def check3(target):
            if len(target) < 3:
                return target
            li = [*target]
            if li[0] == li[1] and li[1] == li[2]:
                return target[:2]
            else:
                return target

        def check4(target):
            if len(target) < 4:
                return target
            li = [*target]
            if li[0] == li[1] and li[2] == li[3]:
                return target[0:3]
            else:
                return target

        def checkAABB(target):
            if len(target) < 4:
                return False
            li = [*target]
            if li[0] == li[1] and li[2] == li[3]:
                return True
            return False

        def checkAAA(target):
            if len(target) < 3:
                return False
            li = [*target]
            if li[0] == li[1] and li[1] == li[2]:
                return True
            return False

        n = int(input())
        for _ in range(n):
            s = input()
            i = 0
            while i < len(s):
                s = s[0:i] + check3(s[i:i+3]) + s[i+3:]
                s = s[0:i] + check4(s[i:i+4]) + s[i+4:]
                if not checkAABB(s[i:i+4]) and not checkAAA(s[i:i+4]):
                    i +=1
            # for i in range(len(s)):
            #     s = s[0:i] + check3(s[i:i+3]) + s[i+3:]
            #     s = s[0:i] + check4(s[i:i+4]) + s[i+4:]
            print(s)

    except:
        break

'''
2
helloo
wooooooow
'''