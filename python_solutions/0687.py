from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = [0]

        def dfs(node: TreeNode) -> int:
            if node == None:
                return 0

            length = 0
            leftLength = dfs(node.left)
            rightLength = dfs(node.right)
            rtr = 0
            if node.left and node.left.val == node.val:
                length += leftLength + 1
                rtr = leftLength + 1
            if node.right and node.right.val == node.val:
                length += rightLength + 1
                rtr = max(rtr, rightLength + 1)

            longest[0] = max(longest[0], length)
            return rtr

        dfs(root)
        return longest[0]


