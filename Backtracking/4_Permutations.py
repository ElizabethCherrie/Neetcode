"""Task 4 Permutations
Given an array nums of unique integers, return all the possible permutations.
You may return the answer in any order."""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return 
            
            for num in nums:
                if num in perm:  
                    continue
                perm.append(num)
                dfs(perm)
                perm.pop()
        dfs([])
        return res