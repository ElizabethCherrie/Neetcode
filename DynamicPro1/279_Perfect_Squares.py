"""Task 279. Perfect Squares

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
"""

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        last = n ** 0.5
        index = 1

        dp[0] = 0
        for i in range(1, n + 1):
            for k in range(1, int(i**0.5) + 1):
                dp[i] = min(dp[i], dp[i - k*k] + 1)

        return dp[n]