from typing import *
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.presum = [[0 for h in range(len(matrix[0]))] for i in range(len(matrix))]
        self.presum[0][0] = matrix[0][0]

        for i in range(1, len(matrix)):
            self.presum[i][0] = self.presum[i - 1][0] + matrix[i][0]
        for j in range(1, len(matrix[0])):
            self.presum[0][j] = self.presum[0][j - 1] + matrix[0][j]
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.presum[i][j] = self.presum[i - 1][j] + self.presum[i][j - 1] - self.presum[i - 1][j - 1] + matrix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.presum[row2][col2]
        if row1 > 0 and col1 > 0:
            return ans + self.presum[row1 - 1][col1 - 1] - self.presum[row1 - 1][col2] - self.presum[row2][col1 - 1]
        elif row1 > 0:
            return ans - self.presum[row1 - 1][col2]
        elif col1 > 0:
            return ans - self.presum[row2][col1 - 1]
        else:
            return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)