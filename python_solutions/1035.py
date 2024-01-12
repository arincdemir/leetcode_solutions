from typing import *

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = dict()

        def dfs(i, j):
            if i >= len(nums1) or j >= len(nums2):
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            ans = 0
            if nums1[i] == nums2[j]:
                ans = 1 + dfs(i + 1, j + 1)

            ans = max(ans, dfs(i + 1, j), dfs(i, j + 1))

            dp[(i, j)] = ans
            return ans

        return dfs(0, 0)

