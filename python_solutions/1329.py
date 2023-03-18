from typing import *
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        ans = [[0 for j in range(m)]for i in range(n)]

        # do the diagonals starting from top
        for i in range(m):
            diagonal = []
            x = i
            y = 0
            while x < m and y < n:
                diagonal.append(mat[y][x])
                x += 1
                y += 1

            diagonal.sort()
            diagonal.reverse()
            x = i
            y = 0
            while x < m and y < n:
                ans[y][x] = diagonal.pop()
                x += 1
                y += 1

        for i in range(n):
            diagonal = []
            x = 0
            y = i
            while x < m and y < n:
                diagonal.append(mat[y][x])
                x += 1
                y += 1

            diagonal.sort()
            diagonal.reverse()
            x = 0
            y = i
            while x < m and y < n:
                ans[y][x] = diagonal.pop()
                x += 1
                y += 1

        return ans

s = Solution()
print(s.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
