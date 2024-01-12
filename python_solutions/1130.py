from typing import *

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = dict()

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == j:
                return 0

            ans = float("inf")
            for k in range(i, j):
                left = dfs(i, k)
                right = dfs(k + 1, j)
                total = left + right + max(arr[i: k + 1]) * max(arr[k + 1: j + 1])
                ans = min(ans, total)

            dp[(i, j)] = ans
            return ans

        return dfs(0, len(arr) - 1)