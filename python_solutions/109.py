from typing import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        mid = self.findMidAndUnlink(head)
        treeNode = TreeNode(mid.val)
        if head == mid:
            return treeNode

        treeNode.right = self.sortedListToBST(mid.next)
        treeNode.left = self.sortedListToBST(head)

        return treeNode

    def findMidAndUnlink(self, head):
        slow = head
        fast = head
        prev = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        return slow
        

