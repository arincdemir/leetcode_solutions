from typing import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = [float("-inf")]
        dp = {}

        def dfs(i):
            if i == len(nums) - 1:
                ans[0] = max(ans[0], nums[-1])
                return (nums[-1], nums[-1])
            
            if i in dp:
                return dp[i]
            
            next = dfs(i + 1)
            elem = nums[i]
            minn = min(elem, next[0] * elem, next[1] * elem)
            maxx = max(elem, next[0] * elem, next[1] * elem)
            ans[0] = max(ans[0], maxx)
            dp[i] = (minn, maxx)
            return dp[i]
        
        dfs(0)
        return ans[0]