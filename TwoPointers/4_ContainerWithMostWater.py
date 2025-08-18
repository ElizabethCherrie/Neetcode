"""Task 4 Container With Most Water
You are given an integer array heights where heights[i] 
represents the height of the i th bar.
You may choose any two bars to form a container. 
Return the maximum amount of water a container can store.
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            new_area = min(heights[l], heights[r]) * (r - l)
            max_area = max(max_area, new_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

        