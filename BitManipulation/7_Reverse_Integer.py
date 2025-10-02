"""Task 7 Reverse Integer
You are given a signed 32-bit integer x.

Return x after reversing each of its digits. After reversing, if x goes outside 
the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0 instead.

Solve the problem without using integers that are outside the signed 32-bit integer range."""

class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            res = (res * 10) + digit

        return res