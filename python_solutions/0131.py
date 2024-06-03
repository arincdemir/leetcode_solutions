from typing import *

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(s: str):
            n = len(s)
            half = n // 2
            for i in range(half):
                if s[i] != s[n - i - 1]:
                    return False
            return True

        def dfs(i, cur, part):
            if i >= len(s):
                if cur == "":
                    ans.append(part.copy())
                return
            
            #add s[i] to cur
            cur += s[i]
            dfs(i + 1, cur, part)
            if isPalindrome(cur):
                part.append(cur)
                dfs(i + 1, "", part)
                part.pop()
        
        dfs(0, "", [])
        return ans

                