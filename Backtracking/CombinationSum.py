"""Task 2  Combination Sum
You are given an array of distinct integers nums and a target integer target.
Your task is to return a list of all unique combinations of nums where the chosen 
numbers sum to target.
The same number may be chosen from nums an unlimited number of times. 
Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
You may return the combinations in any order and the order of the numbers in each combination can be in any order."""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, summ):
            
            if i >= len(nums) or summ > target:
                return

            if summ == target:
                res.append(subset.copy())
                return 

            subset.append(nums[i])
            dfs(i, subset, summ+nums[i])

            subset.pop()
            
            dfs(i+1,subset,summ)

        dfs(0, [], 0)
        return res
