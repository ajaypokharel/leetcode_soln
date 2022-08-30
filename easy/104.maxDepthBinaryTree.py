"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

# BFS
#         q = deque()
        
#         count = 0
        
#         if root:
#             q.append(root)
            
#         while len(q):
            
#             count += 1
                        
#             for _ in range(len(q)):
                
#                 node = q.popleft()                
#                 if node.left:
#                     q.append(node.left)
                    
#                 if node.right:
#                     q.append(node.right)
                            
#         return count

# DFS
        if not root: return 0
    
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1