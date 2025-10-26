"""Task 7 Pacific Atlantic Water Flow

You are given a rectangular island heights where heights[r][c] represents the height
above sea level of the cell at coordinate (r, c).

The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean 
from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell 
with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. 
Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. 
You may return the answer in any order.

"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visited, prev_height):
            if (
                (r, c) in visited
                or r < 0 or c < 0
                or r >= ROWS or c >= COLS
                or heights[r][c] < prev_height
            ):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        # Start from Pacific (top row and left column)
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        # Intersection of cells that can reach both oceans
        res = list(pacific & atlantic)
        return res