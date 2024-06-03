from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(heights)):
            while stack and stack[-1][1] > heights[i]:
                elem = stack.pop()
                left = -1
                if stack:
                    left = stack[-1][0]
                ans = max(ans, elem[1] * (i - left - 1))
            stack.append((i, heights[i]))
        
        while stack:
            elem = stack.pop()
            left = -1
            if stack:
                left = stack[-1][0]
            ans = max(ans, elem[1] * (len(heights) - left - 1))
        
        return ans
