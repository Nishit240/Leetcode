class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(0 , n-1):
            for j in range (i+1, n):
                if nums[i] + nums[j] == target:
                    return[i,j]

        # n = len(nums)
        # hash_map = {}

        # for i in range(n):
        #     remaning = target - nums[i]
        #     if remaning in hash_map:
        #         return [hash_map[remaning], i]
        #     hash_map[nums[i]] = i 




        