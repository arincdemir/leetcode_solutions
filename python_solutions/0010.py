import sys, os



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sys.setrecursionlimit(100000)
        dp = {}

        def dfs(i, j):
            if i == len(s) and j >= len(p):
                return True
            elif j >= len(p):
                return False
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            found = False
            matched = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                found = dfs(i, j + 2) or (matched and dfs(i + 1, j))
            else:
                found = matched and dfs(i + 1, j + 1)
            
            dp[(i, j)] = found
            return found
        
        return dfs(0, 0)
