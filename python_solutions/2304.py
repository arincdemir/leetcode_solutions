from typing import *

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:

        prevRow = grid[0]
        for i in range(1, len(grid)):
            newRow = [float("inf")] * len(prevRow)
            for l in range(len(grid[i - 1])):
                for j in range(len(newRow)):
                    newRow[j] = min(newRow[j], moveCost[grid[i - 1][l]][j] + grid[i][j] + prevRow[l])
            prevRow = newRow

        return min(prevRow)