class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        dummy = []
        lendum = len(nums1) + len(nums2)
        while len(dummy) != lendum:
            if i == len(nums1):
                for a in range (j, len(nums2)):
                    dummy.append(nums2[a])
                break
            elif j == len(nums2):
                for a in range (i, len(nums1)):
                    dummy.append(nums1[a])
                break
            if nums1[i] <= nums2[j]:
                dummy.append(nums1[i])
                i += 1
            else:
                dummy.append(nums2[j])
                j += 1
        mid1 = (lendum-1)//2
        mid2 = lendum // 2
        return((dummy[mid1] + dummy[mid2])/2)