class Solution(object):
    def removeElement(self, nums, val):
        '''
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i
        '''
        k = 0
        for i in range(len(nums)):
           if nums[i]!=val:
               nums[k]=nums[i]
               k+=1
        return k
                
        