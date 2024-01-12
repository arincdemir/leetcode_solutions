from typing import *
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
     
        def bfs(starts):
            queue = deque(starts)
            seen = set(starts)
            while queue:
                elem = queue.popleft()
                h = heights[elem[0]][elem[1]]
                
                for xDirection, yDirection in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    i, j = elem[0] + xDirection, elem[1] + yDirection
                    if (-1 < i < n) and (-1 < j < m) and heights[i][j] >= h and (i, j) not in seen:
                        seen.add((i, j))
                        queue.append((i, j))

            return seen
        
        pacificStarts = []
        for i in range(1, n):
            pacificStarts.append((i, 0))
        for j in range(m):
            pacificStarts.append((0, j))
        pacificTouchers = bfs(pacificStarts)

        atlanticStarts = []
        for i in range(0, n - 1):
            atlanticStarts.append((i, m - 1))
        for j in range(m):
            atlanticStarts.append((n - 1, j))
        atlanticTouchers = bfs(atlanticStarts)

        return list(pacificTouchers.intersection(atlanticTouchers))
            
        
                        
            





                
            
s = Solution()
print(s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))