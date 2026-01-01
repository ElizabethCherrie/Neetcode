"""Task 560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0 : 1}
        total = 0
        curSum = 0

        for num in nums:
            curSum += num
            diff = curSum - k

            total += prefix.get(diff, 0)
            prefix[curSum] = 1 + prefix.get(curSum, 0)

        return total
    