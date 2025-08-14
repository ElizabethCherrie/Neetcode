""" Task 8 Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest 
consecutive sequence of elements that can be formed.
A consecutive sequence is a sequence of elements in which each 
element is exactly 1 greater than the previous element. The elements 
do not have to be consecutive in the original array.
You must write an algorithm that runs in O(n) time.
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count = 1
        maxcount = 0
        if not nums:
            return 0
        for i in range (1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                count += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                if maxcount < count:
                    maxcount = count
                count = 1
        maxcount = max(maxcount, count)
        return maxcount
