from typing import *

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        nums1Sum = sum(nums1)
        nums2Sum = sum(nums2)
        nums1Counts = [0] * 7
        nums2Counts = [0] * 7

        for num in nums1:
            nums1Counts[num] += 1
        for num in nums2:
            nums2Counts[num] += 1

        if nums1Sum == nums2Sum:
            return 0

        fatMan = []
        littleBoy = []
        fatSum = 0
        littleSum = 0
        if nums1Sum < nums2Sum:
            fatSum = nums2Sum
            littleSum = nums1Sum
            for i in range(1, 7):
                for j in range(nums1Counts[i]):
                    littleBoy.append(i)
                for j in range(nums2Counts[i]):
                    fatMan.append(i)
        else:
            fatSum = nums1Sum
            littleSum = nums2Sum
            for i in range(1, 7):
                for j in range(nums1Counts[i]):
                    fatMan.append(i)
                for j in range(nums2Counts[i]):
                    littleBoy.append(i)

        fatIndex = len(fatMan) - 1
        littleIndex = 0
        ans = 0

        while fatSum != littleSum and (
                (littleIndex < len(littleBoy) and littleBoy[littleIndex] != 6) or (fatIndex > -1 and fatMan[fatIndex] != 1)):
            if littleIndex < len(littleBoy) and 6 - littleBoy[littleIndex] >= fatMan[fatIndex] - 1:
                littleSum += min(fatSum - littleSum, 6 - littleBoy[littleIndex])
                littleIndex += 1
            else:
                fatSum -= min(fatSum - littleSum, fatMan[fatIndex] - 1)
                fatIndex -= 1
            ans += 1

        if fatSum == littleSum:
            return ans
        else:
            return -1

s = Solution()
print(s.minOperations([6,6], [1]))