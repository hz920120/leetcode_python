import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        count_map = {}
        for item in nums:
            if item in count_map.keys():
                count_map[item] = count_map[item]+1
            else:
                count_map[item] = 1

        # 定制化一个大根堆，遍历一边数组，最后pop出大根堆最大的两个
        class TopKCount:
            def __init__(self, name, count):
                self.name = name
                self.count = count

            # def __lt__(self, other):
            #     return self.count < other.count

            def __gt__(self, other):
                return self.count < other.count
        heap = []
        for key,value in count_map.items():
            tpc = TopKCount(key, value)
            heapq.heappush(heap, tpc)
        res = [heapq.heappop(heap).name for i in range(k)]
        return res

if __name__ == '__main__':
    qs = [3,0,1,0]
    s = Solution()
    s.topKFrequent(qs, 1)