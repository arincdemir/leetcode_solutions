from typing import *
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        dist = [[float("inf") for j in range(n)] for i in range(n)]
        dist[0][0] = grid[0][0]
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        while heap:
            t, i, j = heapq.heappop(heap)
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if (i, j) == (n - 1, n - 1):
                return t
            
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for x, y in neighbors:
                if x >= 0 and x < n and y >= 0 and y < n:
                    pot = max(t, grid[x][y])
                    if pot < dist[x][y]:
                        heapq.heappush(heap, (pot, x, y))
                        dist[x][y] = pot
            
        
