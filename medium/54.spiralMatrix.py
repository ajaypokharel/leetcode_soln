"""
Given an m x n matrix, return all elements of the matrix in spiral order.

https://leetcode.com/problems/spiral-matrix/
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            for c in range(left, right):
                arr.append(matrix[top][c])

            top += 1

            for r in range(top, bottom):
                arr.append(matrix[r][right - 1])

            right -= 1

            if not (left < right and top < bottom):
                break
            
            for c in range(right - 1, left - 1, -1):
                arr.append(matrix[bottom - 1][c])
            
            bottom -= 1

            for r in range(bottom -1 , top -1, -1):
                arr.append(matrix[r][left])
            
            left += 1
            
        return arr

