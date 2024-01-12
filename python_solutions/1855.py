from typing import *
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        j = len(nums2) - 1
        i = min(len(nums1) - 1, j)
        ans = 0
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                i -= 1
            else:
                j -= 1
                if j < i:
                    i -= 1
        
        return ans

s = Solution()
print(s.maxDistance([2,2,2], [10,10,1]))