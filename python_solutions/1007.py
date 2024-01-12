from typing import *

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        minRotations = float("inf")
        for i in range(1, 7):
            rotations = 0
            successful = True
            for j in range(len(tops)):
                if tops[j] != i:
                    if bottoms[j] == i:
                        rotations += 1
                    else:
                        successful = False
                        break

            if successful:
                minRotations = min(minRotations, rotations)

        for i in range(1, 7):
            rotations = 0
            successful = True
            for j in range(len(tops)):
                if bottoms[j] != i:
                    if tops[j] == i:
                        rotations += 1
                    else:
                        successful = False
                        break

            if successful:
                minRotations = min(minRotations, rotations)

        if minRotations == float("inf"):
            return -1
        else:
            return minRotations