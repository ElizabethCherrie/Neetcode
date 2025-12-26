"""Task 343. Integer Break

Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

Return the maximum product you can get.
"""

class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0 for i in range(n + 1)]
        
        dp[1] = 1
        
        for num in range(n + 1):
            dp[num] = num if num != n else 0
            for i in range(num):
                dp[num] = max(dp[num], dp[i] * dp[num - i])
        
        return dp[n]