import random
import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.array = []
        curNode = head
        while curNode:
            self.array.append(curNode.val)
            curNode = curNode.next

    def getRandom(self) -> int:
        randIndex = math.floor(random.random() * len(self.array))
        return self.array[randIndex]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()