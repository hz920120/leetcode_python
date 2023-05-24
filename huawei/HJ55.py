while True:
    try:
        def check1(x):
            li = str(x)
            for ch in li:
                if ch == '7':
                    return True
            return False

        def check(x):
            if x % 7 == 0:
                return True
            else:
                return check1(x)
        n = int(input())
        res = 0
        for i in range(1, n+1):
            if check(i):
                res += 1

        print(res)
    except:
        break

# if __name__ == '__main__':
#     s = [*'27']
#     print(s)