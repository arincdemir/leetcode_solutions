from typing import *


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        ans = 0

        sortedMatrix = []

        for i in range(n):
            for j in range(m):
                sortedMatrix.append((matrix[i][j], i, j))
        
        sortedMatrix.sort(reverse=True)
        dp = [[0 for j in range(m)] for i in range(n)]

        for val, i, j in sortedMatrix:
            longest = 1
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for x, y in neighbors:
                if x >= 0 and x < n and y >= 0 and y < m and matrix[x][y] > val:
                    longest = max(longest, dp[x][y] + 1)
            dp[i][j] = longest
            ans = max(ans, longest)
        
        return ans