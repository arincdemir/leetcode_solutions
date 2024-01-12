from typing import *
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        connections = dict()

        def dfs(node):
            if node.right:
                connections[node.right.val] = [node.val]
                dfs(node.right)
                connections[node.val].append(node.right.val)
            if node.left:
                connections[node.left.val] = [node.val]
                dfs(node.left)
                connections[node.val].append(node.left.val)

        connections[root.val] = []
        dfs(root)

        ans = []
        queue = deque()
        queue.append((target.val, 0))
        visited = set()
        while queue:
            node, dist = queue.popleft()
            if node in visited:
                continue
            if dist > k:
                break
            visited.add(node)
            if dist == k:
                ans.append(node)
            for con in connections[node]:
                queue.append((con, dist + 1))

        return ans