"""Task 8 Smallest Number With All Set Bits
You are given a positive number n.

Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits

"""

class Solution:
    def smallestNumber(self, n: int) -> int:
        while n & (n + 1):
            n |= n + 1
        return n