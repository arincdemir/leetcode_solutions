from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        leftIn = inorder[:mid]
        rightIn = inorder[mid + 1:]
        leftPre = preorder[1: mid + 1]
        rightPre = preorder[mid + 1:]
        root.left = self.buildTree(leftPre, leftIn)
        root.right = self.buildTree(rightPre, rightIn)

        return root
    
s = Solution()
print(s.buildTree([3,9,20,15,7], [9,3,15,20,7]))