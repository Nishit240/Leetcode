class Solution(object):
    def maxArea(self, height):
        '''
        left = 0
        right = len(height) - 1
        max_area = -1.0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]: 
                left += 1
            else:
                right -= 1

            # left+=1 if height[left] < height[right] else right-=1
        return max_area
        '''
        l, r = 0, len(height) - 1
        res = 0
        maxH = max(height)
        while l < r:
            currentWater = min(height[l], height[r]) * (r-l)
            res = max(res, currentWater)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            if maxH * (r-l) < res:
                break
        return res





        