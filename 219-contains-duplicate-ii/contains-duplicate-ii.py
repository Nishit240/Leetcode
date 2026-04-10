class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool

        """
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                if i - d[nums[i]] <= k:
                    return True
            d[nums[i]] = i
        
        return False 
        # my_set = set()
        # l = r = 0
        # for num in nums:
        #     if num in my_set:
        #         return True
        #     my_set.add(num)
        #     if len(my_set) > k:
        #         my_set.remove(nums[l])
        #         l += 1
        # return False
            




        



        