from typing import *


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums) / 2
        if int(half) != half:
            return False
        
        possibleValues = set([0])

        for i in range(len(nums) - 2, -1, -1):
            for val in possibleValues.copy():
                reachable = val + nums[i]
                if reachable == half:
                    return True
                possibleValues.add(reachable)
        
        return False

        