"""Task 5 Set Matrix Zeroes
Given an m x n matrix of integers matrix, if an element is 0, set its entire row and column to 0's.

You must update the matrix in-place.

Follow up: Could you solve it using O(1) space?

"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
    
        n = len(matrix)
        m = len(matrix[0])
        rowZero = False

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, n):
            for c in range(1, m):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                
        if matrix[0][0] == 0:
            for r in range(n):
                matrix[r][0] = 0
                
        if rowZero:
            for c in range(m):
                matrix[0][c] = 0