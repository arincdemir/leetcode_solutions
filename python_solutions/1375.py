class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = 0
        maxBit = 0
        for i in range(len(flips)):
            maxBit = max(maxBit, flips[i])
            if maxBit == i + 1:
                ans += 1
        
        return ans