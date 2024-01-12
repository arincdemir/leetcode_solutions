from collections import deque
from typing import *

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        ans = [999999999999999]
        nums.sort()
        q = deque(nums)

        def tryPossibilities(removed):
            if removed == 3:
                ans[0] = min(ans[0], q[-1] - q[0])
                return
            
            popped = q.popleft()
            tryPossibilities(removed + 1)
            q.appendleft(popped)
            popped = q.pop()
            tryPossibilities(removed + 1)
            q.append(popped)
        
        tryPossibilities(0)
        return ans[0]
            
s = Solution()
print(s.minDifference([5, 3, 2, 4]))
