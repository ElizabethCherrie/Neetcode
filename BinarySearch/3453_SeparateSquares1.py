"""Task 3453. Separate Squares I

You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point 
and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted multiple times.
"""

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        squares.sort(key = lambda x: (x[1],x[2]))
        total = sum([l*l for _, _, l in squares])
                    
        def solve(pos):
            cur = 0
            for x, y, l in squares:
                if y >= pos:
                    break
                elif pos <= y + l:
                    cur += (pos - y) * l                    
                else:
                    cur += l ** 2
            
            return cur >= total / 2

        l, r = float(squares[0][1]), float(max(y + l for _, y, l in squares))
        
        eps = 1e-5
        while abs(r - l) > eps:
            m = (l + r) / 2
            if solve(m):
                r = m
            else:
                l = m
        
        return round(r, 5)