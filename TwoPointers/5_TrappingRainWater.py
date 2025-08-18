"""Task 5 Trapping Rain Water
You are given an array of non-negative integers height which represent an elevation map. 
Each value height[i] represents the height of a bar, which has a width of 1.
Return the maximum area of water that can be trapped between the bars.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l_val = 0
        max_r_val = 0
        max_area = 0
        while l < r:
            height_l = height[l]
            height_r = height[r]
            max_l_val = max(max_l_val, height_l)
            max_r_val = max(max_r_val, height_r)
            if max_l_val < max_r_val:
                l += 1
                max_area += max_l_val - height_l
            else:
                r -= 1
                max_area += max_r_val - height_r
        return max_area