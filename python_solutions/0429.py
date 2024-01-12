from typing import *
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        lastLevel = -1
        queue = deque()
        if root:
            queue.append((root, 0))
        while len(queue) > 0:
            node, level = queue.popleft()
            if level != lastLevel:
                lastLevel = level
                ans.append([])
            ans[-1].append(node.val)
            for child in node.children:
                queue.append((child, level + 1))

        return ans