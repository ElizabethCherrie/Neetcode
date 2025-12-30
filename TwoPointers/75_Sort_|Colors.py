"""Task 75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        second = 0
        third = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[third] = 2
                nums[second] = 1
                nums[start] = 0
                start += 1
                second += 1
                third += 1
            
            elif nums[i] == 1:
                nums[third] = 2
                nums[second] = 1
                second += 1
                third += 1

            elif nums[i] == 2:
                nums[third] = 2
                third += 1
            
        return nums