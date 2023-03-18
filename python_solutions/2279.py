from typing import *
import heapq
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        empty = [capacity[i] - rocks[i] for i in range(len(capacity))]
        heapq.heapify(empty)
        ans = 0
        while additionalRocks > 0 and ans < len(capacity):
            elem = heapq.heappop(empty)
            if additionalRocks >= elem:
                ans += 1
            additionalRocks -= elem
        return ans

s = Solution()
print(s.maximumBags([2, 3, 4, 5], [1, 2, 4, 4], 2))