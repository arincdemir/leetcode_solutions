from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans = [0]

        def dfs(node, left, length):
            if node is None:
                ans[0] = max(ans[0], length - 1)
                return
            if left:
                dfs(node.left, not left, length + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.left, False, 1)
                dfs(node.right, not left, length + 1)

        dfs(root, True, 0)
        dfs(root, False, 0)
        return ans[0]

