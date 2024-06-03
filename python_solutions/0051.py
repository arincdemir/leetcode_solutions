from typing import *


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def dfs(i: int, usedCols: list, negativeDiagonals: set, positiveDiagonals: set):
            if i == n:
                ans.append([(x, usedCols[x]) for x in range(n)])
                return

            for j in range(n):
                if j not in usedCols and i - j not in negativeDiagonals and i + j not in positiveDiagonals:
                    usedCols.append(j)
                    negativeDiagonals.add(i - j)
                    positiveDiagonals.add(i + j)
                    dfs(i + 1, usedCols, negativeDiagonals, positiveDiagonals)
                    usedCols.pop()
                    negativeDiagonals.remove(i - j)
                    positiveDiagonals.remove(i + j)

        dfs(0, [], set(), set())

        formatted = []
        for placement in ans:
            elem = []
            for i in range(n):
                row = ""
                for j in range(n):
                    if (i, j) in placement:
                        row += "Q"
                    else:
                        row += "."
                elem.append(row)
            formatted.append(elem)

        print(ans)
        return formatted

                