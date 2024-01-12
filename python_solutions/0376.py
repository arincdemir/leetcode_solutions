from typing import *
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        peak = 1
        valley = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                peak = valley + 1
            elif nums[i - 1] > nums[i]:
                valley = peak + 1
        
        return max(peak, valley)
