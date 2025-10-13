"""Task 3 House Robber
You are given an integer array nums where nums[i] represents the amount of money the ith house has. 
The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system 
will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police."""

class Solution:
    def rob(self, nums: List[int]) -> int:

        rew1, rew2 = 0, 0
        
        for num in nums:
            temp = max(num + rew1, rew2)
            rew1 = rew2
            rew2 = temp
        
        return rew2