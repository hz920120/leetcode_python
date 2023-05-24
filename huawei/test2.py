import random
import sys

class Solution:
    # 有序序列的合并
    def merge(self , A, m, B, n):
        p1, p2 = 0, 0




if __name__ == '__main__':
    # A = [random.randint(0, 3) for x in range(10)]
    # B = [random.randint(0, 3) for x in range(10)]
    # A.sort()
    # B.sort()
    A= [4,5,6]
    B=[1,2,3]
    s = Solution()
    print(A)
    print(B)
    s.merge(A,len(A),B, len(B))
    print(A)

