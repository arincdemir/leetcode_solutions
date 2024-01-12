from typing import *

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        nonCaptured = set()

        def dfs(i, j):
            if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) - 1 or board[i][j] == "X" or (i, j) in nonCaptured:
                return
            nonCaptured.add((i, j))
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i, j) not in nonCaptured:
                    board[i][j] = "X"


        