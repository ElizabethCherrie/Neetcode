"""Task 10 Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times."""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        n = len(nums)       
        cur = n / 3
        res = []
        
        max1 = None
        count1 = 0
        
        max2 = None
        count2 = 0
        
        for i in range(n):
            if nums[i] == max1:
                count1 += 1
                
            elif nums[i] == max2:
                count2 += 1
            
            elif count1 == 0:
                max1 = nums[i]
                count1 = 1
                
            elif count2 == 0:
                max2 = nums[i]
                count2 = 1
            
            else:
                count1 -= 1
                count2 -= 1
        
        if nums.count(max1) > cur:
            res.append(max1)
        if nums.count(max2) > cur:
            res.append(max2)
            
        return res