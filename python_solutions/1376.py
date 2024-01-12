from typing import *
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        childrens = {}
        for i in range(n):
            if manager[i] in childrens:
                childrens[manager[i]].append(i)
            else:
                childrens[manager[i]] = [i]
        
        def dfs(node):
            if node not in childrens:
                return 0
            
            ans = 0
            for child in childrens[node]:
                ans = max(ans, dfs(child) + informTime[node])
            
            return ans
    
        return dfs(headID)