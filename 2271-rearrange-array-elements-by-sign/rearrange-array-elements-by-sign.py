class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = [0] * len(nums)
        p = 0
        n = 1

        for i in nums:
            if i >= 0:
                result[p] = i
                p += 2
            else:
                result[n] = i
                n += 2
        return result

        




        