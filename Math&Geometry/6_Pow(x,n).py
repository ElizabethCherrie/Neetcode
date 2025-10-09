"""Task 6 Pow(x, n)
Pow(x, n) is a mathematical function to calculate the value of x raised to the power of n (i.e., x^n).

Given a floating-point value x and an integer value n, implement the myPow(x, n) function, which calculates x raised to the power n.

You may not use any built-in library functions.
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def devcon(x, n):

            if x == 0:
                return 0
            if n == 0:
                return 1

            
            res = devcon(x * x, n // 2)

            return x * res if n % 2 else res

        res = devcon(x, abs(n))
        return res if n >= 0 else 1/res