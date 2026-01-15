"""Task 2943. Maximize Area of Square Hole in Grid

You are given the two integers, n and m and two integer arrays, hBars and vBars. The grid has n + 2 horizontal and m + 2 vertical bars,
creating 1 x 1 unit cells. The bars are indexed starting from 1.

You can remove some of the bars in hBars from horizontal bars and some of the bars in vBars from vertical bars. 
Note that other bars are fixed and cannot be removed.

Return an integer denoting the maximum area of a square-shaped hole in the grid, after removing some bars (possibly none).
"""

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        
        hBars.sort()
        vBars.sort()
        
        hCount = 2
        maxH = 2
        for i in range(1, len(hBars)):
            if hBars[i - 1] + 1== hBars[i]:
                hCount += 1
            else:
                maxH = max(hCount, maxH)
                hCount = 2
        
        vCount = 2
        maxV = 2
        for i in range(1, len(vBars)):
            if vBars[i - 1] + 1 == vBars[i]:
                vCount += 1
            else:
                maxV = max(vCount, maxV)
                vCount = 2
                
        maxH = max(hCount, maxH)
        maxV = max(vCount, maxV)
        
        return min(maxV, maxH) ** 2