class Solution(object):
    def search(self, nums, target):
        l = 0
        h = len(nums) - 1
        while l <= h:
            mid = (l + h) // 2
            if nums[mid] == target:
                return mid
            if nums[h] == target:
                return h
            if nums[l] == target:
                return l
            if nums[mid] <= nums[h]:
                if nums[mid]<=target<=nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
            
            else:
                if nums[l]<=target<=nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
        return -1
            





        