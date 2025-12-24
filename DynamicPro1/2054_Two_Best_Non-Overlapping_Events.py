"""2054. Two Best Non-Overlapping Events

You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei].
The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei.
You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. 
More specifically, if you attend an event with end time t, the next event must start at or after t + 1."""

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        starts = sorted(events)
        ends = sorted(events, key = lambda m: m[1])
        values = sorted(events, key = lambda m: m[2], reverse = True)
        
        best = [0] * n
        best[0] = ends[0][2]
        for i in range(1, n):
            best[i] = max(best[i-1], ends[i][2])
            
        pointer = 0
        maxval = 0
        
        for start, end, value in starts:
            while pointer < n and ends[pointer][1] < start:
                pointer += 1
            
            if pointer > 0:
                maxval = max(maxval, value + best[pointer - 1])
            
            maxval = max(maxval, value)
        
        return maxval
            