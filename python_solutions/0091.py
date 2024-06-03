class Solution:
    def numDecodings(self, s: str, dp = {}) -> int:
        if len(s) == 0:
            return 1
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        if s in dp:
            return dp[s]
        
        ans = 0
        ans += self.numDecodings(s[1:])
        if int(s[:2]) <= 26:
            ans += self.numDecodings(s[2:])
        dp[s] = ans
        return ans
