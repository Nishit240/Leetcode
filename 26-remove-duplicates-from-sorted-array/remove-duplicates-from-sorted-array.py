class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # freq_map= {}
        # for i in range(n):
        #     freq_map[nums[i]] = i 
        # j = 0
        # for k in freq_map:
        #     nums[j] = k
        #     j+=1
        # return j 

        if len(nums) == 1:
            return 1
        i = 0
        j = i+1
        
        while j < len(nums):
            if nums[j] != nums[i]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
            j +=1
        return i+1


            
            








        