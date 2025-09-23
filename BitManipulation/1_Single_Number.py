"""Task 1 Single Number
You are given a non-empty array of integers nums. Every integer appears twice except for one.
Return the integer that appears only once.
You must implement a solution with 
O(n) runtime complexity and use only 
O(1) extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = num ^ result
        return result