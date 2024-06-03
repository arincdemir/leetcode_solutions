from typing import *
import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = [(queries[i], i) for i in range(len(queries))]
        ans = [0] * len(queries)
        queries.sort()

        heap = []
        j = 0
        for query, i in queries:
            while j < len(intervals) and intervals[j][0] <= query:
                heapq.heappush(heap, (intervals[j][1] - intervals[j][0] + 1, intervals[j][1]))
                j += 1
            
            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            if heap:
                ans[i] = heap[0][0]
            else:
                ans[i] = -1

        return ans
            