from typing import *
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x: x[1])
        adjList = defaultdict(list)
        for ticket in tickets:
            llist = adjList[tickets]
            for dest, j

        ans = []

        def dfs(itinerary: list, airport: str):
            if len(itinerary) == len(tickets) + 1:
                ans.append(itinerary.copy())
                return True
            
            temp = adjList[airport].copy()
            for i, dest in enumerate(temp):
                adjList[airport].pop(i)
                itinerary.append(dest)
                if dfs(itinerary, dest):
                    return True
                adjList[airport].insert(i, dest)
                itinerary.pop()
            
            return False
        
        dfs(["JFK"], "JFK")
        return ans[0]