class Solution(object):
    def maxSubArray(self, nums):
        max_v = float('-inf')
        total = 0
        for i in nums:
            total += i
            max_v = max(max_v, total)
            if total < 0:
                total = 0
        return max_v



        