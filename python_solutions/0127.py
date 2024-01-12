from typing import *
import heapq

class Solution:
    def getAdjList(self, wordList):
        patterns = {}
        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                pattern = wordList[i][0:j] + "*" + wordList[i][j + 1:]
                if pattern in patterns:
                    patterns[pattern].append(i)
                else:
                    patterns[pattern] = [i]

        
        adjList = [[] for i in range(len(wordList))]
        for patternInhibitants in patterns.values():
            for i in range(len(patternInhibitants) - 1):
                for j in range(i + 1, len(patternInhibitants)):
                    adjList[patternInhibitants[i]].append(patternInhibitants[j])
                    adjList[patternInhibitants[j]].append(patternInhibitants[i])
        
        return adjList

    def closeTo(self, x, y):
        dist = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                dist += 1
                if dist > 1:
                    return False
        
        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        wordList.append(beginWord)
        adjList = self.getAdjList(wordList)
  
        end = -1
        for i in range(len(wordList)):
            if wordList[i] == endWord:
                end = i

        if end == -1:
            return 0
        
        print(adjList)
        
        
        distances = [float("inf") for i in range(n + 1)]
        distances[n] = 1
        visited = set()
        pq = [(1, n)]
        while pq:
            dist, index = heapq.heappop(pq)
            if index == end:
                return dist
            if index in visited:
                continue
            for edge in adjList[index]:
                if dist + 1 < distances[edge]:
                    distances[edge] = dist + 1
                    heapq.heappush(pq, (dist + 1, edge))

        return 0
