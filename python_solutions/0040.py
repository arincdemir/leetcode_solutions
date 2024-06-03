from typing import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(i, k, cur):
            if k < 0:
                return
            if k == 0:
                ans.append(cur.copy())
            if i >= len(candidates):
                return
            
            if candidates[i] > k:
                return
            cur.append(candidates[i])
            dfs(i + 1, k - candidates[i], cur)
            cur.pop()
            i += 1
            while i < len(candidates) and candidates[i - 1] == candidates[i]:
                i += 1
            dfs(i, k, cur)
        
        dfs(0, target, [])
        return ans

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], target = 8))