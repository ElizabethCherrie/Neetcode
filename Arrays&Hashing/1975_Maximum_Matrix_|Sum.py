"""Task 1975. Maximum Matrix Sum

You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.
"""

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        summa = 0
        nNum = 0
        minim = float("inf")
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                
                if matrix[r][c] < 0:
                    nNum += 1
                    
                minim = min(minim, abs(matrix[r][c]))
                summa += abs(matrix[r][c])
        
        print(minim)
        return summa - minim*2 if nNum % 2 == 1 else summa