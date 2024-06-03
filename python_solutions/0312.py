from typing import *


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}

        def dfs(l, r):
            if l >= r:
                return 0
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            ans = 0
            #imagine I popped the i'th element last
            for i in range(l, r):
                left = dfs(l, i)
                right = dfs(i + 1, r)
                picked = nums[l - 1] * nums[i] * nums[r]
                ans = max(ans, left + right + picked)
            
            dp[(l, r)] = ans
            return ans
        
        nums.insert(0, 1)
        nums.append(1)
        return dfs(1, len(nums) - 1)