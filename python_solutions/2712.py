class Solution:
    def minimumCost(self, s: str) -> int:
        prev = s[0]
        n = len(s)
        ans = 0
        for i in range(1, n):
            if s[i] != prev:
                prev = s[i]
                ans += min(i , n - i)
        
        return ans