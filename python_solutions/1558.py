from typing import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max2Divisions = 0
        ans = 0
        for num in nums:
            divisions = 0
            while num != 0:
                if num % 2 == 0:
                    num = num / 2
                    divisions += 1
                else:
                    num = num - 1
                    ans += 1
            max2Divisions = max(max2Divisions, divisions)

        ans += max2Divisions
        return ans