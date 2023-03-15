from typing import *
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        count = 0
        l = 0
        r = -1
        for i in range(len(nums)):
            if nums[i] < left:
                count += r - l + 1
            elif nums[i] > right:
                l = i + 1
                r = i
            else:
                r = i
                count += r - l + 1
        
        return count
