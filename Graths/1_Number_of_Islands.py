"""Task 1 Number of Islands
Given a 2D grid grid where '1' represents land and '0' represents water, 
count and return the number of islands.
An island is formed by connecting adjacent lands horizontally or vertically and is 
surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water)."""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):

            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == "0":
                return

            grid[row][col] = "0" 

            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row-1, col)
            dfs(row, col-1)
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1

        return count