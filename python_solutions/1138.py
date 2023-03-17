class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        charLocations = {board[i][j]: (i, j) for i in range(5) for j in range(5)}
        charLocations["z"] = (5, 0)
        ans = ""
        curPos = (0, 0)
        for c in target:
            movement = [charLocations[c][0] - curPos[0], charLocations[c][1] - curPos[1]]

            if movement[1] < 0:
                ans += "L" * (-movement[1])
            if movement[0] > 0:
                ans += "D" * movement[0]
            if movement[0] < 0:
                ans += "U" * (-movement[0])
            if movement[1] > 0:
                ans += "R" * movement[1]
            
            curPos = charLocations[c]
            ans += "!"
            

        return ans