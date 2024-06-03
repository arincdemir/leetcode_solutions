from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        elif len(lists) == 0:
            return None
        
        half = len(lists) // 2
        left = self.mergeKLists(lists[0:half])
        right = self.mergeKLists(lists[half:])
        return self.mergeTwoLists(left, right)
                    

    def mergeTwoLists(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        while A or B:
            if A and B:
                if A.val < B.val:
                    cur.next = A
                    A = A.next
                else:
                    cur.next = B
                    B = B.next
            elif A:
                cur.next = A
                A = A.next
            else:
                cur.next = B
                B = B.next
            
            cur = cur.next
        
        return head.next