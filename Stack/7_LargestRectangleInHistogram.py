"""Task 7 Largest Rectangle In Histogram
You are given an array of integers heights where heights[i] 
represents the height of a bar. The width of each bar is 1.
Return the area of the largest rectangle that can be formed among the bars.
Note: This chart is known as a histogram.
"""

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  
        stack = [-1] 
        maxArea = 0 
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea