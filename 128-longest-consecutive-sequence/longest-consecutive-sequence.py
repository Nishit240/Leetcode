class Solution(object):
    def longestConsecutive(self, nums):
        """
         nums.sort()
        count = 0
        last_smaller = float('-inf')
        longest = 0

        for i in nums:
            num = i
            if num-1 ==last_smaller:
                count += 1
                last_smaller = num
            elif num != last_smaller:
                count = 1
                last_smaller = num
            longest = max(longest,count)
        return longest
        """
        
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                count = 1

                while current + 1 in num_set:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest






                

        