class Solution:
    def solution(self, ages):
        if not ages:
            return 0

        res = 0
        for x in range(len(ages)):
            for y in range(len(ages)):
                if x == y:
                    continue
                if ages[y] <= 0.5 * ages[x] + 7 or ages[y] > ages[x] or (ages[y] > 100 and ages[x] < 100):
                    continue
                else:
                    res += 1
        return res


    def solution1(self, ages):
        if not ages:
            return 0

        ages.sort()
        # ages = ages[::-1]
        res = 0
        for x in range(len(ages)):
            for y in range(x+1, len(ages)):
                val = 0
                if ages[x] < 100:
                    val = max(max(0.5 * ages[x] + 7, ages[y]), 99)
                else:
                    val = max(max(0.5 * ages[x] + 7, ages[y]), 100)




        return res

if __name__ == '__main__':
    s = Solution()
    ages = [20, 30, 100, 110, 120]
    a = s.solution(ages)
    print(a)