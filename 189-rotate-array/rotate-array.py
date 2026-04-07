class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # rotation = k % n

        # for _ in range(rotation):
        #     e = nums.pop()
        #     nums.insert(0,e)

        k = k % len(nums)
        nums[:] = nums[-k: ] + nums[ :-k]
        return nums


        