"""Task 2 Jump Game

You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.

"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        best_Jump = nums[0]
        
        for start in range(1, len(nums)):
            best_Jump -= 1

            if best_Jump < 0:
                return False

            if start + best_Jump >= len(nums) - 1:
                return True
            else:
                best_Jump = max(best_Jump, nums[start])

        return False
