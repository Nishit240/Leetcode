class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        my_set = set()
        l = r = 0
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
            if len(my_set) > k:
                my_set.remove(nums[l])
                l += 1
        return False
        """
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                if i - my_dict[nums[i]] <= k:
                    return True
            my_dict[nums[i]] = i
        
        return False 
            




        



        