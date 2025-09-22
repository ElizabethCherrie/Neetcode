"""Task 4 Kth Largest Element in an Array
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.
By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.
Follow-up: Can you solve it without sorting?"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)

        for i in range(k - 1):
            heapq.heappop(maxHeap)

        return -maxHeap[0]
