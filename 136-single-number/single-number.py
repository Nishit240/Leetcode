class Solution(object):
    def singleNumber(self, nums):
        """
        result = 0
        for num in nums:
            result ^= num
        return result
        """
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:
            if freq[num] == 1:
                return num