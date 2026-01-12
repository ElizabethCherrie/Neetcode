"""Task 1283. Find the Smallest Divisor Given a Threshold

Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. 
Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer."""

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        def divRes(div):
            res = 0
            for i in nums:
                res += math.ceil(i / div)
            
            return res <= threshold
        
        l, r = 1, max(nums)
        ans = 0

        while l <= r:
            m = (r + l) // 2
            
            if divRes(m):
                r = m - 1
                ans = m
            
            else:
                l = m + 1
            
        return ans