"""Task 1 Best Time to Buy and Sell Stock
You are given an integer array prices where prices[i] is the price of 
NeetCoin on the ith day. You may choose a single day to buy one NeetCoin and 
choose a different day in the future to sell it.
Return the maximum profit you can achieve. You may choose to
not make any transactions, in which case the profit would be 0."""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_pr = prices[0]
        max_pr = 0
        for price in prices:
            profit = price - min_pr
            min_pr = min(min_pr, price)
            max_pr = max(max_pr, profit)
        return max_pr