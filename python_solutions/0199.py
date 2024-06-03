from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        maxHeight = [-1]
        ans = []

        def traverse(height: int, node: Optional[TreeNode]):

            if not node:
                return

            if height > maxHeight[0]:
                maxHeight[0] = height
                ans.append(node.val)
            
            traverse(height + 1, node.right)
            traverse(height + 1, node.left)
        
        traverse(0, root)
        return ans