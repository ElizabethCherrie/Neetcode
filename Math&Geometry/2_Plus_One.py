"""Task 2 Plus One
You are given an integer array digits, where each digits[i] is the ith digit of a large integer. 
It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
                
            digits[i] = 0

        return [1] + digits