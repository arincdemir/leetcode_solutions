from typing import *

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rowHashes = dict()

        for row in grid:
            tupRow = tuple(row)
            rowHashes[tupRow] = rowHashes.get(tupRow, 0) + 1

        ans = 0

        for j in range(len(grid[0])):
            tupCol = []
            for i in range(len(grid)):
                tupCol.append(grid[i][j])

            tupCol = tuple(tupCol)
            ans += rowHashes.get(tupCol, 0)

        return ans