from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], rules=[float("-inf"), float("inf")]) -> bool:
        if not root:
            return True
        
        if rules[0] < root.val < rules[1]:
            leftRules = [rules[0], min(rules[1], root.val)]
            rightRules = [max(rules[0], root.val), rules[1]]
            return self.isValidBST(root.left, leftRules) and self.isValidBST(root.right, rightRules)
        else:
            return False
        