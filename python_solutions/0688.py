class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

        dp = dict()
        def prob(numMoves, x, y):
            if x < 0 or x >= n or y < 0 or y >= n:
                return 0
            if numMoves == k:
                return 1
            if (numMoves, x, y) in dp:
                return dp[(numMoves, x, y)]
            curProb = 0
            for move in moves:
                curProb += prob(numMoves + 1, x + move[0], y + move[1])
            curProb /= 8
            dp[(numMoves, x, y)] = curProb
            return curProb

        return prob(0, row, column)