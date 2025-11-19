"""Task 12 Partition Equal Subset Sum
You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where 
sum(subset1) == sum(subset2). Otherwise, return false."""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = sum(nums) // 2
        dp = [False for i in range(target + 2)]
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]