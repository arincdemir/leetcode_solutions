from typing import *

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1])
        maxEndingBefore = [(events[0][2], events[0][1])]
        for i in range(1, len(events)):
            maxEndingBefore.append((max(events[i][2], maxEndingBefore[i - 1][0]), events[i][1]))

        events.sort(key=lambda x: x[0], reverse=True)
        maxStartingAfter = [(events[0][2], events[0][0])]
        for i in range(1, len(events)):
            maxStartingAfter.append((max(events[i][2], maxStartingAfter[i - 1][0]), events[i][0]))


        ans = 0
        for start, end, val in events:
            l = 0
            r = len(maxEndingBefore) - 1
            while l < r:
                mid = (l + r + 1) // 2
                elem = maxEndingBefore[mid][1]
                if elem < start:
                    l = mid
                else:
                    r = mid - 1

            maxLeft = maxEndingBefore[l][0]
            if maxEndingBefore[l][1] >= start:
                maxLeft = 0

            l = 0
            r = len(maxEndingBefore) - 1
            while l < r:
                mid = (l + r) // 2
                elem = maxStartingAfter[mid][1]
                if elem > end :
                    r = mid
                else:
                    l = mid + 1

            maxRight = maxStartingAfter[l][0]
            if maxStartingAfter[l][1] <= end:
                maxRight = 0

            ans = max(ans, val + maxRight, val + maxLeft)

        return ans

s = Solution()
print(s.maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))