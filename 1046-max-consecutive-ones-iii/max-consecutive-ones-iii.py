class Solution(object):
    def longestOnes(self, nums, k):
        """
        l = 0
        r = 0
        max_l = 0
        zeros = 0
        while (r < len(nums)):
            if nums[r] == 0:
                zeros += 1
            while(zeros > k ):
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                max_l = max(max_l, r-l+1)
            r += 1
        return max_l
        left=0
        zero_count=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero_count+=1
            if zero_count>k:
                if nums[left]==0:
                    zero_count-=1
                left+=1
        return len(nums)-left
        """
        l = 0
        r = 0
        max_l = 0
        zeros = 0
        while (r < len(nums)):
            if nums[r] == 0:
                zeros += 1
            if (zeros > k ):
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            if zeros <= k:
                max_l = max(max_l, r-l+1)
            r += 1
        return max_l




               
            
            


        


        