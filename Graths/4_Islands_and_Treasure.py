"""Task 4 Islands and Treasure
You are given a m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach 
a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        visited = set()
        q = deque()

        def nextStop(row, col):
            if (row < 0 or col < 0 or row == rows or col == cols
            or (row, col) in visited or grid[row][col] == -1):
                return

            visited.add((row, col))
            q.append([row, col])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append([row, col])
                    visited.add((row, col))

        trip = 0
        while q:
            for i in range(len(q)):

                r, c = q.popleft()

                grid[r][c] = trip
                
                nextStop(r + 1, c)
                nextStop(r - 1, c)
                nextStop(r, c + 1)
                nextStop(r, c - 1)

            trip += 1