from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [float("-inf")]

        def maxSinglePath(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left = maxSinglePath(node.left)
            right = maxSinglePath(node.right)
            merged = left + right + node.val
            ans[0] = max(ans[0], merged)
            
            return max(0, left + node.val, right + node.val)

        maxSinglePath(root)
        return ans[0]