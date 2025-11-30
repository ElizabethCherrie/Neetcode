"""Task 1590 Make Sum Divisible by P

Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that
the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.
"""

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        
        target = total % p
        
        if target == 0:
            return 0

        prefix = 0
        n = len(nums)
        res = n
        seen = {0: -1} 

        for i, num in enumerate(nums):
            prefix = (prefix + num) % p

            need = (prefix - target) % p
            if need in seen:
                res = min(res, i - seen[need])
            seen[prefix] = i

        return res if res < n else -1       