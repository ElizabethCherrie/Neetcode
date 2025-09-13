"""Task 4 Subsets II
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.
The solution must not contain duplicate subsets. You may return the solution in any order."""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, subset):

            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1, subset)
            
        dfs(0, [])
        return res