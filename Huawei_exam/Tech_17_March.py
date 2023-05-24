class Solution:
    def s1(self, strs):
        if not str:
            return 0
        strs = [*strs]
        bucket = [0]*26
        for ch in strs:
            if ch not in bucket:
                bucket[ord(ch) - ord('A')] += 1

        res = 0
        divided = 1
        for i in range(len(bucket)):
            res += bucket[i]
            j = bucket[i]
            while j > 0:
                divided *= j
                j -= 1

        d = 1
        while res > 0:
            d *= res
            res -= 1
        return d // divided


if __name__ == '__main__':
    s = Solution()
    print(s.s1('ABCDEFGHHA'))
