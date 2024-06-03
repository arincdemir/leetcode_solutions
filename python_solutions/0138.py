from typing import *

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldNodesIndexes = {}
        newNodes = []
        newRandomIndexes = []

        cur = head
        i = 0
        while cur:
            oldNodesIndexes[cur] = i
            newNodes.append(Node(cur.val))
            newRandomIndexes.append(cur.random)
            i += 1
            cur = cur.next
        
        newNodes.append(None)
        oldNodesIndexes[None] = len(newNodes) - 1
        
        newRandomIndexes = [oldNodesIndexes[elem] for elem in newRandomIndexes]


        for i in range(len(newNodes) - 1):
            newNodes[i].next = newNodes[i + 1]
            newNodes[i].random = newNodes[newRandomIndexes[i]]
        
        return newNodes[0]
