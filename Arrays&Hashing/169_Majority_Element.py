"""Task 169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        maxi = nums[0]
        maxC = 1

        for i in range(1, len(nums)):
            if nums[i] == maxi:
                maxC += 1

            elif maxC == 0:
                maxi = nums[i]
            
            else:
                maxC -= 1
        
        return maxi