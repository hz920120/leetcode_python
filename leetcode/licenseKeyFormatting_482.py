class Solution:
    def licenseKeyFormatting(self, s: str, k: int):
        if s == "" or len(s) <= k:
            return s.replace("-", "").upper()

        s = s.replace("-", "").upper()
        first = len(s) % k

        res = ""
        if first != 0:
            res += s[0: first]
            res += "-"
            s = s[first:]
        index = 0
        for i in range(len(s) + 1):
            if i != 0 and (i % k == 0):
                res += s[index: i]
                if i != len(s): res += "-"
                index = i

        return res


s = Solution()
print(s.licenseKeyFormatting("2-5g-3-J", 2))
