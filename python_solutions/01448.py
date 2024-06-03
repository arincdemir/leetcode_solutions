from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode, maxSoFar=float("-inf")) -> int:
        if not root:
            return 0
        
        ans = 1 if root.val >= maxSoFar else 0
        maxSoFar = max(root.val, maxSoFar)
        ans += self.goodNodes(root.right, maxSoFar) + self.goodNodes(root.left, maxSoFar)
        return ans