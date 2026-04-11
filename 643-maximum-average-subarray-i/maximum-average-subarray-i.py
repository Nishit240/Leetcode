class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = 0
        for i in range(k):
            sums += nums[i]
        
        maxsum = sums
        l = 0
        r = k
        while r < len(nums):
            sums -= nums[l]
            l += 1
            sums += nums[r]
            r += 1
            maxsum = max(maxsum, sums)
        return float(maxsum) / k



        