class Solution(object):
    def fourSum(self, nums, target):
        ans = []
        if len(nums) < 4:
            return []
        nums.sort()
        if nums[0] + nums[1] + nums[2] + nums[3] > target:
            return []
        if nums[-1] + nums[-2] + nums[-3] + nums[-4] < target:
            return []
        for i in range(len(nums) - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[-3] + nums[-2] + nums[-1] < target:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1
        return ans












            
        