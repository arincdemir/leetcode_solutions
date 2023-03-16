from typing import *
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2WIndexes = [(nums2[i], i) for i in range(len(nums2))]
        nums2WIndexes.sort(key=lambda x: x[0])
        ans = [-1] * len(nums1)
        unused = []
        j = 0
        for i in range(len(nums1)):
            if nums1[i] > nums2WIndexes[j][0]:
                ans[nums2WIndexes[j][1]] = nums1[i]
                j += 1
            else:
                