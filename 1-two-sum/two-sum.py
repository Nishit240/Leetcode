class Solution(object):
    def twoSum(self, nums, target):
        """
        n = len(nums)
        for i in range(0 , n-1):
            for j in range (i+1, n):
                if nums[i] + nums[j] == target:
                    return[i,j]
        """

        # n = len(nums)
        # hash_map = {}

        # for i in range(n):
        #     remaning = target - nums[i]
        #     if remaning in hash_map:
        #         return [hash_map[remaning], i]
        #     hash_map[nums[i]] = i 

        i = 0
        while i < len(nums):
            two = target - nums[i]
            if two in nums:
                if nums.index(two) < i:
                    return [nums.index(two), i]
                elif nums.index(two) > i:
                    return [i, nums.index(two)]
            i += 1
        return []




        