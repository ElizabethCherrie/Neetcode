""" Task 3 Two Sum
Given an array of integers nums and an integer target, return 
the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of i
ndices i and j that satisfy the condition.
Return the answer with the smaller index first.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]