class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # def f(i):
        #     if i >= len(nums):
        #         return 0
        #     if nums[i] == -1:
        #         return 0
        #     if i == len(nums) - 1 and nums[0] == -1:
        #         return 0
        #     # if value[i] > 0:
        #     #     return value[i]
        #     cur_value = nums[i]
        #     nums[i] = -1
        #     get = f(i + 2) + cur_value
        #     nums[i] = cur_value
        #     not_get = f(i + 1)
        #     if get > not_get:
        #         return get
        #     else:
        #         return not_get
        #
        # return f(0)

        # get_list = [0] * len(nums)
        # not_get_list = [0] * len(nums)
        # def f1(i):
        #     if i >= len(nums):
        #         return 0
        #     if nums[i] == -1:
        #         return 0
        #     if i == len(nums) - 1 and nums[0] == -1:
        #         return 0
        #     if get_list[i] > 0 and not_get_list[i] > 0:
        #         return max(get_list[i], not_get_list[i])
        #     cur_value = nums[i]
        #     nums[i] = -1
        #     get = f1(i + 2) + cur_value
        #     nums[i] = cur_value
        #     not_get = f1(i + 1)
        #     if get > not_get:
        #         get_list[i] = get
        #         return get
        #     else:
        #         not_get_list[i] = not_get
        #         return not_get
        #
        # return f1(0)

        valid = [0] * len(nums)
        def valid_max_index():
            max_value = 0
            res = -1
            for index, i in enumerate(nums):
                if valid[index] == 0:
                    if nums[index] > max_value:
                        max_value = nums[index]
                        res = index
            return res

        def delete_relate(index):
            left = index-1
            right = 0 if index == len(nums) - 1 else index+1
            valid[index] = 1
            valid[left] = 1
            valid[right] = 1


        def f2(value):
            max_index = valid_max_index()
            if max_index == -1:
                return value
            value += nums[max_index]
            delete_relate(max_index)
            return f2(value)



        return f2(0)


if __name__ == '__main__':
    s = Solution()
    print(s.rob([94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]))