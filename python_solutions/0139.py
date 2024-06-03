from typing import *


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)

        dp = {}

        def breakable(i):
            if i >= len(s):
                return True
            
            if i in dp:
                return dp[i]
            
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in wordDict:
                    if breakable(j):
                        dp[i] = True
                        return True
            
            dp[i] = False
            return False
        
        return breakable(0)

