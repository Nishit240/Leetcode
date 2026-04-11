class Solution(object):
    def findMaxAverage(self, nums, k):
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
        """
        c_sum = sum(nums[:k])
        max_sum = c_sum

        for i in range(k, len(nums)):
            c_sum += nums[i] - nums[i - k]
            if c_sum > max_sum:
                max_sum = c_sum
        return float(max_sum) / k 
        



        