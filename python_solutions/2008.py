from typing import *
from collections import defaultdict
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        ridesThatStartAt = defaultdict(list)
        # create ridesThatStartAt with end and money values
        for s, e, t in rides:
            ridesThatStartAt[s].append((e, e - s + t))

        dp = {}
        def dfs(i):
            if i == n:
                return 0
            
            if i in dp:
                return dp[i]
            
            # do not take any rides, skip the spot
            skip = dfs(i + 1)

            # take the rides available
            take = 0
            for e, m in ridesThatStartAt[i]:
                take = max(take, dfs(e) + m)
            
            maxValue = max(skip, take)
            dp[i] = maxValue
            return maxValue
        
        return dfs(1)
