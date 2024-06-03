from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if fast: # if odd number of nodes, start from the smaller part
            slow = slow.next
        
        cur = slow
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        right = prev
        left = head
        cur = head
        while right:
            leftNext = left.next
            rightNext = right.next
            cur.next = left
            left.next = right
            cur = right
            left = leftNext
            right = rightNext
        
        if fast: #odd
            cur.next = left
            left.next = None

        
        