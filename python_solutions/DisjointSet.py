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
