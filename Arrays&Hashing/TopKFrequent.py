"""Task 5 Top K Frequent Elements
Given an integer array nums and an integer k, return the k most 
frequent elements within the array.
The test cases are generated such that the answer is always unique.
You may return the output in any order.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}

        for i in nums:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1

        count_dict = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

        output = []
        for i in range(k):
            output.append(count_dict[i][0])

        return output