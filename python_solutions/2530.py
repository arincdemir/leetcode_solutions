from typing import *
import math
import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)

        for _ in range(k):
            maxx = -heapq.heappop(nums)
            ans += maxx
            heapq.heappush(nums, -math.ceil(maxx / 3))

        return ans