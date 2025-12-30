"""Task 304. Range Sum Query 2D - Immutable

Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by
its upper left corner (row1, col1) and lower right corner (row2, col2).
You must design an algorithm where sumRegion works on O(1) time complexity.
"""

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = []

        if not matrix or not matrix[0]:
            return

        for row in range(len(self.matrix)):
            sub = []
            for col in range(len(self.matrix[0])):
                top = self.prefix[row - 1][col] if row > 0 else 0
                left = sub[col - 1] if col > 0 else 0
                top_left = self.prefix[row - 1][col - 1] if row > 0 and col > 0 else 0

                sub.append(
                    self.matrix[row][col] + top + left - top_left
                )

            self.prefix.append(sub)
       
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            
        bigRec = self.prefix[row2][col2]
        leftRec = self.prefix[row2][col1 - 1] if col1 > 0 else 0
        topRec = self.prefix[row1 - 1][col2] if row1 > 0 else 0
        shared = self.prefix[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0

        return bigRec - leftRec - topRec + shared

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)