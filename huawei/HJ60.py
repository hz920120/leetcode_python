while True:
    try:
        def check(n):
            i = 3
            while i <= (n - 1):
                r = n % i
                if r == 0:
                    return False
                else:
                    i += 1
            return True


        n = int(input())

        mid = n // 2
        if check(mid):
            print(mid)
            print(mid)
        else:
            if mid % 2 == 0:
                for i in range(mid):
                    step = 2 * i + 1
                    if check(mid - step) and check(mid + step):
                        print(mid - step)
                        print(mid + step)
                        break
            else:
                for i in range(mid):
                    step = 2 * i
                    if check(mid - step) and check(mid + step):
                        print(mid - step)
                        print(mid + step)
                        break
    except:
        break


# def check(n):
#     if n == 2:
#         return True
#     i = 2
#     while i <= (n - 1):
#         r = n % i
#         if r == 0:
#             return False
#         else:
#             i += 1
#     return True
#
# print(check(4))