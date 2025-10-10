""" Task 7 Multiply Strings

You are given two strings num1 and num2 that represent non-negative integers.

Return the product of num1 and num2 in the form of a string.

Assume that neither num1 nor num2 contain any leading zero, unless they are the number 0 itself.

Note: You can not use any built-in library to convert the inputs directly into integers.

"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def Multiply(num1: str, digit: str) -> str:
            carry = 0
            result = []

            for i in range(len(num1) - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(digit) - ord('0')) + carry
                result.append(str(product % 10))

                carry = product // 10

            if carry:
                result.append(str(carry))

            return ''.join(reversed(result))

        def addStrings(num1: str, num2: str) -> str:
            i, j = len(num1) - 1, len(num2) - 1
            carry = 0
            res = []

            while i >= 0 or j >= 0 or carry:
                x = ord(num1[i]) - ord('0') if i >= 0 else 0
                y = ord(num2[j]) - ord('0') if j >= 0 else 0

                total = x + y + carry

                res.append(str(total % 10))

                carry = total // 10

                i -= 1
                j -= 1
                
            return ''.join(reversed(res))

        res = "0"
        zeros = 0

        for j in range(len(num2) - 1, -1, -1):
            partial = Multiply(num1, num2[j]) + ("0" * zeros)
            
            res = addStrings(res, partial)
            zeros += 1

        return res
