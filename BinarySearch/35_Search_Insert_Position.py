"""Task 35. Search Insert Position

You are given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            print(l,r,m)
            if target < nums[m]:
                r = m - 1
            elif target == nums[m]:
                return m
            else:
                l = m + 1

        return l