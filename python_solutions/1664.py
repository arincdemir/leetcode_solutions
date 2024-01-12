from typing import *

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        cumSum = []
        odds = 0
        evens = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                evens += nums[i]
                cumSum.append(evens)
            else:
                odds += nums[i]
                cumSum.append(odds)

        sumAfter = []
        odds = 0
        evens = 0
        for i in range(len(nums) - 1, -1, -1):
            if i % 2 == 0:
                evens += nums[i]
                sumAfter.append(evens)
            else:
                odds += nums[i]
                sumAfter.append(odds)

        sumAfter.reverse()

        ans = 0
        for i in range(len(nums)):
            evens = sumAfter[i] - nums[i]
            if i > 0:
                evens += cumSum[i - 1]

            odds = cumSum[i] - nums[i]
            if i < len(nums) - 1:
                odds += sumAfter[i + 1]

            if odds == evens:
                ans += 1

        return ans

        return 0