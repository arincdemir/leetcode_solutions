from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    preIndex = 0
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        node = TreeNode(preorder[self.preIndex])
        self.preIndex += 1

        if self.preIndex < len(preorder):
            nextVal = preorder[self.preIndex]
            if postorder.index(nextVal) < postorder.index(node.val):
                node.left = self.constructFromPrePost(preorder, postorder)

        if self.preIndex < len(preorder):
            nextVal = preorder[self.preIndex]
            if postorder.index(nextVal) < postorder.index(node.val):
                node.right = self.constructFromPrePost(preorder, postorder)

        return node