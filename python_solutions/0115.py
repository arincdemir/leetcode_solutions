class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}


        def distinct(i, j):
            if i == len(s):
                if j == len(t):
                    return 1
                else:
                    return 0
            
            if j == len(t):
                return 1
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            ans = 0
            ans += distinct(i + 1, j)
            if s[i] == t[j]:
                ans += distinct(i + 1, j + 1)
            
            dp[(i, j)] = ans
            return ans
        
        return distinct(0, 0)
