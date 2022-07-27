class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i, val in enumerate(numbers):
            other = target - val
            if other in map:
                index = map.get(other)
                return [i+1, index+1] if i <= index else [index+1, i+1]
            map[val] = i