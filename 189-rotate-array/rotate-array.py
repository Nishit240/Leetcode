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

        n = len(nums)
        k %= n 
        nums[:] = nums[n-k:] + nums[ :n-k]


        