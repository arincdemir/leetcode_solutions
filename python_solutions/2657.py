from typing import *

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen = [False] * (len(B) + 1)
        ans = []
        x = 0
        for i in range(len(A)):
            if seen[A[i]]:
                x += 1
            else:
                seen[A[i]] = True
            if seen[B[i]]:
                x += 1
            else:
                seen[B[i]] = True
            ans.append(x)

        return ans

