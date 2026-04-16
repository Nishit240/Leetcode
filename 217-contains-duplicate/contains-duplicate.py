class Solution(object):
    def containsDuplicate(self, nums):
        '''
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        '''
        return len(list(set(nums)))<len(nums)
