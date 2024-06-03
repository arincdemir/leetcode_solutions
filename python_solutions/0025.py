from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        newHead = ListNode()
        newCur = newHead
        forward = head
        while forward:
            nodes = []
            successful = True
            for i in range(k):
                if not forward:
                    successful = False
                    break
                nodes.append(forward)
                forward = forward.next
            
            if successful:
                newCur.next = nodes[-1]
                for i in range(k - 1, 0, -1):
                    nodes[i].next = nodes[i - 1]
                newCur = nodes[0]
                newCur.next = None
            else:
                newCur.next = nodes[0]
        
        return newHead.next



