class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        rows = [0] * n
        columns = [0] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i] += 1
                    columns[j] += 1
    
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if rows[i] > 1 or columns[j] > 1:
                        count += 1
        
        return count