"""Task 9 N-Queens
The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
so that no two queens can attack each other.
A queen in a chessboard can attack horizontally, vertically, and diagonally.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a unique board layout where the queen pieces are placed. 
'Q' indicates a queen and '.' indicates an empty space.
You may return the answer in any order."""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]

        def dfs(row):
            if row == n:
                cur = ["".join(r) for r in board]
                res.append(cur)
                return
            for col in range(n):
                if self.noQ(row, col, board):
                    board[row][col] = "Q"
                    dfs(row + 1)
                    board[row][col] = "."
        dfs(0)
        return res        
        
    def noQ(self, row, col, board):
        curr, curc = row, col

        while curr >= 0:
            if board[curr][curc] == "Q":
                return False
            curr -= 1

        curr, curc = row, col

        while curr >= 0 and curc >= 0:
            if board[curr][curc] == "Q":
                return False
            curr, curc = curr - 1, curc - 1

        curr, curc = row, col

        while curr >= 0 and curc < len(board):
            if board[curr][curc] == "Q":
                return False
            curr, curc = curr - 1, curc + 1

        return True