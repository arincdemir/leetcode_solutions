from typing import *

class DisjointSet:
    def __init__(self):
        self.parents = dict()

    def union(self, x, y):
        x = self.findAncestor(x)
        y = self.findAncestor(y)
        if y != x:
            self.parents[y] = x

    def find(self, x, y):
        return self.findAncestor(x) == self.findAncestor(y)

    def findAncestor(self, x):
        if x not in self.parents:
            return x
        ancestor = self.findAncestor(self.parents[x])
        self.parents[x] = ancestor
        return ancestor


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        ds = DisjointSet()
        for x, y in allowedSwaps:
            ds.union(x, y)

        components = dict()
        for i in range(len(source)):
            if ds.findAncestor(i) not in components:
                components[ds.findAncestor(i)] = dict()
            components[ds.findAncestor(i)][source[i]] = components[ds.findAncestor(i)].get(source[i], 0) + 1
            components[ds.findAncestor(i)][target[i]] = components[ds.findAncestor(i)].get(target[i], 0) - 1

        ans = 0
        for elements in components.values():
            positives = 0
            negatives = 0
            for val in elements.values():
                if val < 0:
                    negatives += -val
                else:
                    positives += val
            ans += max(positives, negatives)

        return ans

