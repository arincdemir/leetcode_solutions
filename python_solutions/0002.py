from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        prev = head
        carry = 0
        while l1 or l2 or carry == 1:
            addition = 0
            if l1 and l2:
                addition = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                addition = l1.val + carry
                l1 = l1.next
            elif l2:
                addition = l2.val + carry
                l2 = l2.next
            else:
                addition = 1
            
            carry = 0
            if addition >= 10:
                carry = 1
                addition = addition % 10
            newNode = ListNode(addition)
            prev.next = newNode
            prev = newNode

        return head.next

            
