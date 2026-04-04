class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # i = 0
        # j = i + 1
        # k = j + 1
        # n = len(nums)
        # result = set()
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1 , n):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp = [nums[i], nums[j], nums[k]]
        #                 temp.sort()
        #                 result.add(tuple(temp))
        # return list(result)

        result = set()
        n = len(nums)

        for i in range(n):
            my_set = set()
            for j in range(i + 1, n):
                th = -(nums[i] + nums[j])

                if th in my_set:
                    temp = [nums[i], nums[j], th]
                    temp.sort()
                    result.add(tuple(temp))
                else:
                    my_set.add(nums[j])

        return list(result)








                             







        