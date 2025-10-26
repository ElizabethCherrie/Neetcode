"""Task 6 Rotting Fruit
You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, 
then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. 
If this state is impossible within the grid, return -1.

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque([])
        fresh = 0
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    q.append((row, col, 0))
                elif grid[row][col] == 1:
                    fresh += 1

        maxminutes = 0

        while q:
            row, col, minutes = q.popleft()
            print(maxminutes, minutes)

            maxminutes = max(maxminutes, minutes)

            for ar, ac in directions:
                nr, nc = row + ar, col + ac
                if -1 < nr < ROWS and -1 < nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 2 
                    fresh -= 1
                    q.append((nr, nc, minutes + 1))

        return maxminutes if fresh == 0 else -1
