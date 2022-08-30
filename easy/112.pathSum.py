"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

https://leetcode.com/problems/path-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        return self.dfs(root, targetSum)
    
    def dfs(self, root, targetSum):
        
        if root:
        
            node = root

            rem = targetSum - node.val
            
            if not node.left and not node.right:
                if rem == 0:
                    return True

            return self.dfs(node.left, rem) or self.dfs(node.right, rem)