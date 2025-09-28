"""Task 2 Max Area of Island
You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

An island is defined as a group of 1's connected horizontally or vertically.
You may assume all four edges of the grid are surrounded by water.

The area of an island is defined as the number of cells within the island.

Return the maximum area of an island in grid. If no island exists, return 0. """

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_len = 0
        count = 0
        cols = len(grid[0])
        rows = len(grid)
        res = []

        def dfs(row, col):
            nonlocal max_len
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            max_len = 1
            max_len += dfs(row + 1, col)
            max_len += dfs(row, col + 1)
            max_len += dfs(row - 1, col)
            max_len += dfs(row, col - 1)

            return max_len

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    res.append(area)

        return max(res) if res else 0