from typing import *

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n, m = len(board), len(board[0])

        def dfs(i, j, wordLeft, visited):
            if i < 0 or i >= n or j < 0 or j >= m or (i,j) in visited or board[i][j] != wordLeft[0]:
                return False
            
            wordLeft = wordLeft[1:]
            if wordLeft == "":
                return True
            visited.add((i, j))
            if (dfs(i - 1, j, wordLeft, visited) or dfs(i + 1, j, wordLeft, visited) or
                dfs(i, j - 1, wordLeft, visited) or dfs(i, j + 1, wordLeft, visited)):
                return True
            visited.remove((i, j))
            return False
            

        for i in range(n):
            for j in range(m):
                if dfs(i, j, word, set()):
                    return True
        
        return False