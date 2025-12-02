"""Task 3 Jump Game II

You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i.
For example, if you are at nums[i], you can jump to any index i + j where:

j <= nums[i]
i + j < nums.length
You are initially positioned at nums[0].

Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). 
You may assume there is always a valid answer.
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        min_n_Jumps = 0
        best_Jump = 0
        start = 0

        for i in range(len(nums) - 1):
            
            best_Jump = max(best_Jump, i + nums[i])
            
            if i == start:
                min_n_Jumps += 1
                start = best_Jump
            
            if start >= len(nums) - 1:
                return min_n_Jumps
        
        return min_n_Jumps