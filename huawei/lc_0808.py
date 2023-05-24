class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        chars = []
        for ch in S:
            chars.append(ch)
        res = []
        visited = []


        def dfs(li: list, pre: str) -> None:
            if len(li) == 1 and (pre + li[0]) not in visited:
                res.append(pre + li[0])
                visited.append(pre + li[0])
                return
            for i, val in enumerate(li):
                new_li = li.copy()
                c = new_li[i]
                if pre + c in visited:
                    continue
                else:
                    visited.append(pre + c)
                    new_li.pop(i)
                    dfs(new_li, pre + c)

        dfs(chars, '')
        return res



            # 添加visited，并剪枝
            # for c in li:
            #     if (pre + c) in visited:
            #         li.remove(c)
            #     else:
            #         visited.append(pre + c)
            # for i in range(len(li)):
            #     new_li = li.copy()
            #     new_li.pop(i)
            #     return dfs(new_li, pre + li[0])

if __name__ == '__main__':
    s = Solution()
    print(s.permutation('abccd'))