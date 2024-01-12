from typing import *

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        lastFreshOranges = -1
        curFreshOranges = self.freshOrangesLeft(grid)

        if curFreshOranges == 0:
            return 0

        while lastFreshOranges != curFreshOranges:
            self.rot(grid)
            lastFreshOranges = curFreshOranges
            curFreshOranges = self.freshOrangesLeft(grid)
            minute += 1
        
        if curFreshOranges == 0:
            return minute - 1
        else:
            return -1

    
    def freshOrangesLeft(self, grid) -> int:
        n, m = len(grid), len(grid[0])
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                
        return fresh
    
    def rottenNearby(self, grid, i, j) -> bool:
        n, m = len(grid), len(grid[0])
        return ((i - 1 >= 0 and grid[i - 1][j] == 2) or (i + 1 < n and grid[i + 1][j] == 2) or 
                (j - 1 >= 0 and grid[i][j - 1] == 2) or (j + 1 < m and grid[i][j + 1] == 2))
        
    
    def rot(self, grid) -> None:
        n, m = len(grid), len(grid[0])
        indexes = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if self.rottenNearby(grid, i, j):
                        indexes.append((i, j))
        
        for index in indexes:
            grid[index[0]][index[1]] = 2
                    
    