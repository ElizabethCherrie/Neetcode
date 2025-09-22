"""Task 3 K Closest Points to Origin
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane.
You are also given an integer k.
Return the k closest points to the origin (0, 0).
The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
You may return the answer in any order.
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = ((x ** 2) + (y ** 2)) ** 0.5
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])

        return res