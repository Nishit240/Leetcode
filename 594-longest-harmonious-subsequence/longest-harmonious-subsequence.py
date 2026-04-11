class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = Counter(nums)
        res = 0
        for i in nums:
            if i+1 in nums:
                res = max(res, (nums[i] + nums[i+1]))
        return res
            

             



            


        