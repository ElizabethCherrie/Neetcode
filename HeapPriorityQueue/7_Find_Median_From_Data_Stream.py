"""Task 7 Find Median From Data Stream
The median is the middle value in a sorted list of integers. For lists of even length,
there is no middle value, so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far."""

class MedianFinder:

    def __init__(self):
        self.median = []

    def addNum(self, num: int) -> None:
        self.median.append(num)

    def findMedian(self) -> float:
        self.median.sort()
        mid = len(self.median)
        if mid % 2 != 0:
            res = self.median[mid // 2]
        else:
            res = (self.median[mid//2] + self.median[mid // 2 - 1]) / 2
        return res 
        