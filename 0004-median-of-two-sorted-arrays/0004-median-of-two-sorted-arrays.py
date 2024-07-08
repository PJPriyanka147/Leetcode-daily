class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0 , 0

        #merge the two arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        #appending remaining elements of nums1 
        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        #appending remaining elements of nums2
        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        #finding the median
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n//2])
        else:
            return float(merged[(n//2) - 1] + merged[n//2]) / 2.0

        