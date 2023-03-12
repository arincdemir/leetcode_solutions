from typing import *
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Create an adjacency list and add neighboring genes
        adjacencyList = {}
        bank.append(startGene)
        for gene in bank:
            neighbors = []
            for gene2 in bank:
                if gene != gene2:
                    difference = 0
                    for i in range(8):
                        if gene[i] != gene2[i]:
                            difference += 1
                    if difference == 1:
                        neighbors.append(gene2)

            adjacencyList[gene] = neighbors
    
        q = deque()
        q.append((startGene, 0))
        visited = set()
        while len(q) > 0:
            gene, dist = q.popleft()
            if gene == endGene:
                return dist
            visited.add(gene)
            for neighbor in adjacencyList[gene]:
                if neighbor not in visited:
                    q.append((neighbor, dist + 1))
        
        return -1



        
        

