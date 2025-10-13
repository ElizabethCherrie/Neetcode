"""Task 1 Climbing Stairs
You are given an integer n representing the number of steps to reach the top of a staircase. 
You can climb with either 1 or 2 steps at a time.

Return the number of distinct ways to climb to the top of the staircase."""

class Solution:
    def climbStairs(self, n: int) -> int:
        
        first = (1 + 5 ** 0.5) / 2
        second =  (1 - 5 ** 0.5) / 2
    
        n += 1

        return round((first**n - second**n) / 5 ** 0.5)