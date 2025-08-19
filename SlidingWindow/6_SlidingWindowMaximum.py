"""Task 6 Sliding Window Maximum
You are given an array of integers nums and an integer k. 
There is a sliding window of size k that starts at the left edge of the array.
The window slides one position to the right until it reaches the right edge of the array.
Return a list that contains the maximum element in the window at each step.
"""

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr_max = 0
        window = collections.deque()
        maxs = []
        for r in range (len(nums)):
            while window and nums[r] > nums[window[-1]]:
                window.pop()
            window.append(r)

            if window[0] <= r - k:
                window.popleft()

            if r >= k - 1:
                curr_max = nums[window[0]]
                maxs.append(curr_max)
        return maxs
