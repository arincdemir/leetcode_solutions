from typing import *
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()
        
        def putToQueue(queue: deque, val):
            while queue and val > queue[-1]:
                queue.pop()
            queue.append(val)

        for i in range(k):
            putToQueue(queue, nums[i])
        ans.append(queue[0])

        for right in range(k, len(nums)):
            putToQueue(queue, nums[right])
            left = right - k + 1
            if queue[0] == nums[left - 1]:
                queue.popleft()
            ans.append(queue[0])
            
        return ans
            

        