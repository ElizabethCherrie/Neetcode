"""Task 2 Make Array Elements Equal to Zero
You are given an integer array nums.

Start by selecting a starting position curr such that nums[curr] == 0, 
and choose a movement direction of either left or right.

After that, you repeat the following process:

If curr is out of the range [0, n - 1], this process ends.
If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right,
or decrementing curr if you are moving left.
Else if nums[curr] > 0:
Decrement nums[curr] by 1.
Reverse your movement direction (left becomes right and vice versa).
Take a step in your new direction.
A selection of the initial position curr and movement direction is considered valid 
if every element in nums becomes 0 by the end of the process.

Return the number of possible valid selections.
"""

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)
        
        res = 0
        for num in nums:
            if num == 0:
                if 0 <= left_sum - right_sum <= 1:
                    res += 1
                if 0 <= right_sum - left_sum <= 1:
                    res += 1
            else:
                left_sum += num
                right_sum -= num
        return res
