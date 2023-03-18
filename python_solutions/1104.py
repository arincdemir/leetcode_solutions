from typing import *
import math
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if math.floor((math.log2(label))) % 2 == 1:
            label = 3 * 2**math.floor((math.log2(label))) - label - 1
        ans = []
        while label > 0:
            ans.append(label)
            label = label // 2
        
        ans.reverse()
        for i in range(1, len(ans), 2):
            ans[i] = 3 * 2**i - ans[i] - 1
        
        return ans