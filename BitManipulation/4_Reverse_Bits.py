"""Task 4 Reverse Bits
Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res += (bit << (31 - i))
        return res