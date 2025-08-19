"""Task 3 Koko Eating Bananas
You are given an integer array piles where piles[i] is the number
of bananas in the ith pile. You are also given an integer h,
which represents the number of hours you have to eat all the bananas. 
You may decide your bananas-per-hour eating rate of k. Each hour,
you may choose a pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, you may finish eating the pile 
but you can not eat from another pile in the same hour.
Return the minimum integer k such that you can eat all the bananas within h hours."""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(float(p) / mid)
            if time > h:
                l = mid + 1
            else:
                k = mid
                r = mid - 1
        return k