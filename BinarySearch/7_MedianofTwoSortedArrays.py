"""Task 7 Median of Two Sorted Arrays
You are given two integer arrays nums1 and nums2 of size m and n respectively, 
where each is sorted in ascending order.
Return the median value among all elements of the two arrays.
Your solution must run in
O(log(m+n)) time."""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ful_len = len(nums1) + len(nums2)
        half = (ful_len + 1) // 2
        
        if len(nums1) <= len(nums2):
            smaller, larger = nums1, nums2
        else:
            smaller, larger = nums2, nums1

        l1, r1 = 0, len(smaller)

        while l1 <= r1:
            mid = (r1 + l1) // 2
            leftover = half - mid

            smaller_l  = smaller[mid - 1] if mid > 0 else float("-inf")
            smaller_r = smaller[mid] if mid < len(smaller) else float("inf")
            larger_l = larger[leftover - 1] if leftover > 0 else float("-inf")
            larger_r = larger[leftover] if leftover < len(larger) else float("inf")

            if smaller_l <= larger_r and larger_l <= smaller_r:
                left_max  = max(smaller_l, larger_l)
                right_min = min(smaller_r, larger_r)
                return float(left_max) if ful_len % 2 else (left_max + right_min) / 2

            if smaller_l > larger_r:
                r1 = mid - 1
            else:
                l1 = mid + 1