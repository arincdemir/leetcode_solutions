from typing import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = [num for num in nums if num != val]
        for i in range(len(ans)):
            nums[i] = ans[i]
        return len(ans)