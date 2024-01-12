from typing import *

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        ans = 0
        zeroFound = False
        posIndex = len(fruits)
        negIndex = -1
        for i in range(len(fruits)):
            if fruits[i][0] == startPos:
                negIndex = i - 1
                posIndex = i + 1
                zeroFound = True
                break
            elif fruits[i][0] > startPos:
                posIndex = i
                negIndex = i - 1
                break
        
        cumSums = [0 for i in range(len(fruits))]
        if negIndex >= 0:
            cumSums[negIndex] = fruits[negIndex][1]
        if posIndex < len(fruits):
            cumSums[posIndex] = fruits[posIndex][1]
        
        for i in range(negIndex - 1, -1, -1):
            cumSums[i] = cumSums[i + 1] + fruits[i][1]
        for i in range(posIndex + 1, len(fruits)):
            cumSums[i] = cumSums[i - 1] + fruits[i][1]
        
        print(cumSums)
        for i in range(negIndex, -1, -1):
            if startPos - fruits[i][0] > k:
                break
            if (startPos - fruits[i][0]) * 2 >= k:
                ans = max(ans, cumSums[i])
                break
            rangee = k - fruits[i][0] * 2
            left = posIndex
            right = len(fruits) - 1
            while left < right:
                mid = (left + right) // 2
                pos = fruits[mid][0]


        return ans

s = Solution()
s.maxTotalFruits([[2,8],[6,3],[8,6]], 5, 4)