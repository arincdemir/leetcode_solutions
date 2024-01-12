from typing import *

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:

        dp = {}
        n = len(tasks)

        def dfs(mask, remaining):
            if mask == (1 << n) - 1:
                return 0
            
            if (mask, remaining) in dp:
                return dp[(mask, remaining)]
            
            ans = 999999
            for i in range(n):
                if mask & (1 << i) == 0:
                    if tasks[i] <= remaining:
                        newMask = mask | (1 << i)
                        ans = min(ans, dfs(newMask, remaining - tasks[i]))
                    else:
                        newMask = mask | (1 << i)
                        ans = min(ans, 1 + dfs(newMask, sessionTime - tasks[i]))
            
            dp[(mask, remaining)] = ans
            return ans
        
        return dfs(0, 0)