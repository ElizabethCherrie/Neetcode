# Task1 Contains Duplicate
# Given an integer array nums, return true if any value appears 
# more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        double = []
        for i in nums:
            if i in double:
                return True
            else:
                double.append(i)
        return False