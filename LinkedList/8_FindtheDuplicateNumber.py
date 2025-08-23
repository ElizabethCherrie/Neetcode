"""Task 8 Find the Duplicate Number
You are given an array of integers nums containing n + 1 integers. 
Each integer in nums is in the range [1, n] inclusive.
Every integer appears exactly once, except for one integer
which appears two or more times. Return the integer that appears more than once.
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] *= -1
            else:
                return abs(nums[i])