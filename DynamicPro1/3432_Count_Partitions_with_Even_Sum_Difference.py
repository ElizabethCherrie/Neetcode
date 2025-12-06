"""3432 Count Partitions with Even Sum Difference

You are given an integer array nums of length n.

A partition is defined as an index i where 0 <= i < n - 1, splitting the array into two non-empty subarrays such that:

Left subarray contains indices [0, i].
Right subarray contains indices [i + 1, n - 1].
Return the number of partitions where the difference between the sum of the left and right subarrays is even.

"""

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        sumL = 0
        sumR = sum(nums)
        counter = 0

        for i in nums:
            if abs(sumL - sumR) % 2 == 0:
                counter+=1
                
            sumL += i
            sumR -= i

        return counter - 1 if counter else counter