class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        my_set = set()
        l = r = 0
        for num in nums:
            if num in my_set:
                return True
            my_set.add(num)
            if len(my_set) > k:
                my_set.remove(nums[l])
                l += 1
        return False
            




        



        