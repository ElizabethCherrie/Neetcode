"""Task 3315. Construct the Minimum Bitwise Array II

You are given an array nums consisting of n prime integers.

You need to construct an array ans of length n, such that, for each index i, the bitwise OR of ans[i] and ans[i] + 1 is equal to nums[i], 
i.e. ans[i] OR (ans[i] + 1) == nums[i].

Additionally, you must minimize each value of ans[i] in the resulting array.

If it is not possible to find such a value for ans[i] that satisfies the condition, then set ans[i] = -1.
"""

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                ans[i] = nums[i] - (((nums[i] + 1) & (-nums[i] - 1)) // 2)
                
        return ans