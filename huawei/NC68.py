


class Solution:
    def jumpFloor(self, number):
        # write code here
        map = {}
        def m(number):
            if number in map:
                return map[number]
            if number > 1:
                total = m(number - 1) + m(number - 2)
                map[number] = total
                return total
            else:
                return 1
        return m(number)



if __name__ == '__main__':
    s = Solution()
    print(s.jumpFloor(35))