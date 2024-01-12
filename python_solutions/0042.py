from typing import *

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        cumSum = [height[0]]
        for i in range(1, n):
            cumSum.append(cumSum[i - 1] + height[i])
        
        maxIndex = height.index(max(height))

        left = 0
        right = 1
        while left < maxIndex:
            if height[right] < height[left]:
                right += 1
            else:
                clutter = cumSum[right - 1] - cumSum[left]
                rectangle = (right - left - 1) * min(height[right], height[left])
                ans += rectangle - clutter
                left = right
                right += 1
        

        left = n - 2
        right = n - 1
        while right > maxIndex:
            if height[left] < height[right]:
                left -= 1
            else:
                clutter = cumSum[right - 1] - cumSum[left]
                rectangle = (right - left - 1) * min(height[right], height[left])
                ans += rectangle - clutter
                right = leftw
                left -= 1

        return ans