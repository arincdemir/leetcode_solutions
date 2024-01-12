from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        elif head.next == None:
            return head

        # divide list into two parts and disconnect them
        prev = head
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merge(left, right)

    def merge(self, n1: ListNode, n2: ListNode) -> ListNode:
        start = None
        if n1.val < n2.val:
            start = n1
            n1 = n1.next
        else:
            start = n2
            n2 = n2.next

        cur = start
        while n1 and n2:
            if n1.val < n2.val:
                cur.next = n1
                cur = n1
                n1 = n1.next
            else:
                cur.next = n2
                cur = n2
                n2 = n2.next

        if n1:
            cur.next = n1
        else:
            cur.next = n2

        return start

