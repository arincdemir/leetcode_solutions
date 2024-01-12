from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head.next
        total = 0
        nodes = []
        while cur:
            if cur.val == 0:
                nodes.append(total)
                total = 0
            else:
                total += cur.val
            cur = cur.next

        newListHead = ListNode(nodes[0])
        cur = newListHead
        for i in range(1, len(nodes)):
            newNode = ListNode(nodes[i])
            cur.next = newNode
            cur = newNode

        return newListHead