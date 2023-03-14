from typing import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sums = []
        total = self.sumOfSubTrees(root, sums)
        half = total / 2
        closestSplit = 0
        minDiff = 99999999
        for s in sums:
            if abs(total - s) < minDiff:
                minDiff = abs(total - s)
                closestSplit = s
        
        product = closestSplit * (total - closestSplit)

        return product % (10 ** 9 + 7)

    def sumOfSubTrees(self, root, sums):
        if root == None:
            return 0
        
        mySum = root.val + self.sumOfSubTrees(root.left, sums) + self.sumOfSubTrees(root.right, sums)
        root.sums = mySum
        sums.append(mySum)
        return mySum