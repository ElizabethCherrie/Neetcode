"""Task 9 Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product within the array and return it.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currmin = 1
        currmax = 1

        for num in nums:
            newmax = num * currmax
            newmin = num * currmin
    
            currmax, currmin = (max(newmin, num, newmax), 
            min(newmin, num, newmax))

            res = max(res, currmax)

        return res