from typing import *

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(k):
            if k < 0:
                return float("inf")
            if k == 0:
                return 0
            if k in dp:
                return dp[k]
            
            ans = float("inf")
            for coin in coins:
                if coin <= k:
                    ans = min(ans, dfs(k - coin) + 1)
            
            dp[k] = ans
            return ans
        
        rtr = dfs(amount)
        if rtr == float("inf"):
            return -1
        return rtr