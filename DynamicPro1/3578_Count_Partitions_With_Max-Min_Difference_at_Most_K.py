"""Task 3578 Count Partitions With Max-Min Difference at Most K

You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty
contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.

Return the total number of ways to partition nums under this condition.

Since the answer may be too large, return it modulo 109 + 7.

"""

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        from collections import deque
        mx, mn = deque(), deque()
        
        l = 0
        s = 0
        
        for r in range(n):
            while mx and nums[mx[-1]] <= nums[r]:
                mx.pop()
            while mn and nums[mn[-1]] >= nums[r]:
                mn.pop()
            mx.append(r)
            mn.append(r)
            
            while nums[mx[0]] - nums[mn[0]] > k:
                if mx[0] == l:
                    mx.popleft()
                if mn[0] == l:
                    mn.popleft()
                s = (s - dp[l]) % MOD
                l += 1
            
            s = (s + dp[r]) % MOD
            dp[r + 1] = s
        
        return dp[n]