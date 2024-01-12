from typing import *
import copy

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        def score(mat):
            for row in mat:
                if row[0] == 1:
                    continue
                else:
                    for i in range(len(row)):
                        row[i] = 1 if row[i] == 0 else 0

            for j in range(len(mat[0])):
                ones = 0
                for i in range(len(mat)):
                    ones += mat[i][j]
                if ones >= len(mat) - ones:
                    continue
                else:
                    for i in range(len(mat)):
                        mat[i][j] = 1 if mat[i][j] == 0 else 0

            ans = 0
            for row in mat:
                for j in range(len(row)):
                    row[j] = str(row[j])
            for row in mat:
                ans += int("".join(row), 2)

            return ans

        without = score(copy.deepcopy(grid))
        for row in grid:
            row[0] = 1 if row[0] == 0 else 0
        withh = score(grid)
        return max(withh, without)


s = Solution()
print(s.matrixScore([[0,0,0],[0,1,0],[0,1,0],[0,1,1],[0,0,0],[1,1,0],[1,0,1],[0,1,0],[0,0,1]]))