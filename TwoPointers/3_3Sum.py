"""Task 3 3Sum
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.
The output should not contain any duplicate triplets.
You may return the output and the triplets in any order."""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, first in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            if first > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while l < r:
                second = nums[l]
                third = nums[r]
                threesum = first + second + third
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    result.append([first, second, third])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return result