class Solution(object):
    def majorityElement(self, nums):
        """
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
        """
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1 
        for i in nums:
            if hashmap[i] > len(nums) // 2:
                return i

        