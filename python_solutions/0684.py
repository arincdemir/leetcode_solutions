from DisjointSet import DisjointSet

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disj = DisjointSet()
        for edge in edges:
            if disj.find(edge[0], edge[1]):
                return edge
            else:
                disj.union(edge[0], edge[1])