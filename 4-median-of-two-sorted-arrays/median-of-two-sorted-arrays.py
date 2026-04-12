class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        '''
        nums3 = []
        i, j = 0, 0
        n, m = len(nums1), len(nums2)

        # Merge step
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        # Remaining elements
        while i < n:
            nums3.append(nums1[i])
            i += 1

        while j < m:
            nums3.append(nums2[j])
            j += 1

        # Median calculation
        k = len(nums3)
        if k % 2 == 1:
            return float(nums3[k // 2])
        else:
            return (nums3[k // 2 - 1] + nums3[k // 2]) / 2.0
        '''

        mergedList = nums1 + nums2
        sortedList = sorted(mergedList)
        n = len(sortedList)

        if n % 2 == 0:
            return (sortedList[n//2 - 1] + sortedList[n//2]) / 2.0
        else:
            return sortedList[n//2]