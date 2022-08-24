class Cards:
    def cardGame(self, A, n):
        # write code here
        def first(arr, l, r):
            if l == r:
                return arr[l]
            # 先拿左边
            l_max = arr[l] + second(arr, l+1, r)
            # 先拿右边
            r_max = arr[r] + second(arr, l, r-1)

            return max(l_max, r_max)

        def second(arr, l, r):
            if l == r:
                return 0
            l_min = first(arr, l+1, r)
            r_min = first(arr, l, r-1)
            return min(l_min, r_min)

        return max(first(A, 0, n-1), second(A, 0, n-1))


if __name__ == '__main__':
    s = Cards()
    s.cardGame([19,11,45,45,43,0,77,78,86,50,40,12,35,26,35,3,58,24,63,79,23,59,8,64,99,68,35,28,61,72,54,30,50,70,40,52,82,34,8,9,46,22,84,67,70,56,11,59,54,60,97,38,0,90,81,44,75,76,74,86,73,90,53,70,56,92,50,84,95,9,6,50,39,32,14,93,1,72],78)