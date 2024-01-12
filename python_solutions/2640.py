from typing import *

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        maxBefore = [nums[0]]
        for i in range(1, len(nums)):
            maxBefore.append(max(maxBefore[i - 1], nums[i]))

        conv = []
        for i in range(len(nums)):
            conv.append(maxBefore[i] + nums[i])

        ans = [conv[0]]
        for i in range(1, len(nums)):
            ans.append(conv[i] + ans[i - 1])

        return ans