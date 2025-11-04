"""Task 8 Find X-Sum of All K-Long Subarrays I
You are given an array nums of n integers and two integers k and x.

The x-sum of an array is calculated by the following procedure:

Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, 
the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].
"""

from collections import Counter
import heapq
from typing import List

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:

        pos = 0
        ans = []

        while pos + k <= len(nums):
            sub = nums[pos: pos + k]
            
            freq = Counter(sub)
            max_heap = [(-count, -num, num) for num, count in freq.items()]
            heapq.heapify(max_heap)

            total = 0

            for _ in range(min(x, len(max_heap))):
                count, _, num = heapq.heappop(max_heap)
                total += (-count) * num

            ans.append(total)

            pos += 1
        return ans