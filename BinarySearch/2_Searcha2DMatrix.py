"""Task 2 Search a 2D Matrix
You are given an m x n 2-D integer array matrix and an integer target.
Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.
Can you write a solution that runs in O(log(m * n)) time?"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: 
            return False

        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = l + (r - l) // 2
            row, col = divmod(mid, COLS)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False