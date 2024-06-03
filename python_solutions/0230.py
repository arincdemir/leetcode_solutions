from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [-1]

        def numOfNodes(node: Optional[TreeNode], k):
            if not node:
                return 0
            
            left = numOfNodes(node.left, k)
            if left >= k:
                return k + 1
            current = left + 1
            if current == k:
                ans[0] = node.val
                return current

            right = numOfNodes(node.right, k - current)
            return current + right
        
        numOfNodes(root, k)
        return ans[0]