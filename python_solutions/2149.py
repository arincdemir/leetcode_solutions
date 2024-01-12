from typing import *

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for num in nums:
            if num < 0:
                negatives.append(num)
            else:
                positives.append(num)

        ans = []
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(positives[i // 2])
            else:
                ans.append(negatives[i // 2])

        return ans