"""Task 2 Two Integer Sum II
Given an array of integers numbers that is sorted in non-decreasing order.
Return the indices (1-indexed) of two numbers, [index1, index2], such 
that they add up to a given target number target and index1 < index2. 
Note that index1 and index2 cannot be equal, therefore you may not 
use the same element twice.
There will always be exactly one valid solution.
Your solution must use 
O(1) additional space.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        first = numbers[l]
        second = numbers[r]
        while l < r:
            first = numbers[l]
            second = numbers[r]
            if first + second < target:
                l += 1
            elif first + second > target:
                r -= 1
            else:
               return [l + 1, r + 1]