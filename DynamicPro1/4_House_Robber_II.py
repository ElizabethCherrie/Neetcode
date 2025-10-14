"""Task 4 House Robber II
You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because 
the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police."""

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def maxFinder(nums):

            firstSum, secondSum = 0, 0

            for i in nums:

                maxx = max(firstSum + i, secondSum)

                firstSum = secondSum
                secondSum = maxx
            
            return secondSum
        
        if len(nums) == 1: 
            return nums[0]

        return max(maxFinder(nums[1:]), maxFinder(nums[:-1]))
