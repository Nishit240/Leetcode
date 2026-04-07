class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        m,count = 0,0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count +=1
                m = max(m,count)
            else:
                count = 0
        return m
            
        


        