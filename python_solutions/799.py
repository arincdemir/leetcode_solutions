from typing import *
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        curRow = [poured]
        for i in range(query_row):
            newRow = [0] * (i + 2)
            for j in range(len(curRow)):
                pour = curRow[j] - 1
                if pour > 0:
                    half = pour / 2
                    newRow[j] += half
                    newRow[j + 1] += half
            
            curRow = newRow
        
        if curRow[query_glass] > 1:
            return 1
        else:
            return curRow[query_glass]
