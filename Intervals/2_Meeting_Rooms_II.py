"""Task 2 Meeting Rooms II

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8."""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        intervals.sort(key = lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end)
            
        return len(min_heap)