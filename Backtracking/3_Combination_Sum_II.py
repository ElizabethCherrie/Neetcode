"""Task 3 Combination Sum II
You are given an array of integers candidates, which may contain duplicates,
and a target integer target. Your task is to return a list of all unique combinations 
of candidates where the chosen numbers sum to target.
Each element from candidates may be chosen at most once within a combination. 
The solution set must not contain duplicate combinations.
You may return the combinations in any order and the order of the numbers in each 
combination can be in any order.
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def dfs(i, subset, summ):
            
            if summ == target:
                res.append(subset.copy())
                return
            if i == len(candidates) or summ > target:
                return
            print(subset)
            print(summ)

            subset.append(candidates[i])
            dfs(i + 1, subset, summ + candidates[i])
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, subset, summ)

        dfs(0, [], 0)
        return res