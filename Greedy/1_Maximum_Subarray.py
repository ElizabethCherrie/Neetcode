"""Task 1 Maximum Subarray

Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res, cur_sum = nums[0], 0

        for i in nums:
            cur_sum += i
            res = max(res, cur_sum)

            if cur_sum < 0:
                cur_sum = 0

        return res