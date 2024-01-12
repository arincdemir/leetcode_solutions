from typing import *
import math

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def tryH(h):
            l = 0
            r = len(citations) - 1
            if citations[r] >= h:
                while l < r:
                    mid = (l + r) // 2
                    if citations[mid] >= h:
                        r = mid
                    else:
                        l = mid + 1

                if len(citations) - l >= h:
                    return True
                else:
                    return False

            else:
                return False


        l = 0
        r = 1000
        while l < r:
            mid = math.ceil((l + r) / 2)
            works = tryH(mid)
            if works:
                l = mid
            else:
                r = mid - 1

        return l

s = Solution()
print(s.hIndex([100]))