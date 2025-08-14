"""Task 6 Products of Array Except Self
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].Each product is guaranteed to fit in a 32-bit integer.
Follow-up: Could you solve it in O(n)
O(n) time without using the division operation?"""

import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerocount = nums.count(0)
    
        if zerocount > 1:
            return [0] * len(nums)
    
        fulproduct = math.prod([n for n in nums if n != 0])
        output = [0] * len(nums)
        
        if zerocount == 0:
            for i in range(len(nums)):
                output[i] = fulproduct // nums[i]
        else:
            zero_index = nums.index(0)
            output[zero_index] = fulproduct
        
        return output