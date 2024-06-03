from typing import *


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[-1] = 1
        ans = 1
        for i in range(len(nums) - 2, -1, -1):
            maxx = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    maxx = max(maxx, dp[j] + 1)
            
            dp[i] = maxx
            ans = max(ans, maxx)

        return ans
