class Solution(object):
    def findLHS(self, nums):
        '''
        nums = Counter(nums)
        res = 0
        for i in nums:
            if i+1 in nums:
                res = max(res, (nums[i] + nums[i+1]))
        return res
        '''
        my_dict = {}
        for element in nums:
            if element not in my_dict:
                my_dict[element] = 1
            else:
                my_dict[element] += 1
        max = 0
        for key in my_dict:
            if (key + 1 in my_dict) and (my_dict[key] + my_dict[key + 1] > max):
                max = (my_dict[key] + my_dict[key + 1])
        return max





            

             



            


        