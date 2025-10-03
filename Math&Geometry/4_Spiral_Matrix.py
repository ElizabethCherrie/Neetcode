"""Task 4 Spiral Matrix
Given an m x n matrix of integers matrix, return a list of all elements within the matrix in spiral order.
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []

        def turn(top, bottom, left, right):
            print(res)

            if top > bottom or left > right:
                return 

            for i in range(left, right + 1):
                res.append(matrix[top][i])

            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])

            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][i])

            if left < right:
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])


            return turn(top + 1, bottom - 1, left + 1, right - 1)
            
        turn(0, m - 1, 0, n - 1)
        return res