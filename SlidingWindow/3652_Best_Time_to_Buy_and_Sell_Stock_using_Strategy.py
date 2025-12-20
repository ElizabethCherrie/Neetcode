"""Task 3652. Best Time to Buy and Sell Stock using Strategy

You are given two integer arrays prices and strategy, where:

prices[i] is the price of a given stock on the ith day.
strategy[i] represents a trading action on the ith day, where:
-1 indicates buying one unit of the stock.
0 indicates holding the stock.
1 indicates selling one unit of the stock.
You are also given an even integer k, and may perform at most one modification to strategy. A modification consists of:

Selecting exactly k consecutive elements in strategy.
Set the first k / 2 elements to 0 (hold).
Set the last k / 2 elements to 1 (sell).
The profit is defined as the sum of strategy[i] * prices[i] across all days.

Return the maximum possible profit you can achieve.

Note: There are no constraints on budget or stock ownership, so all buy and sell operations are feasible regardless of past actions.

"""

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        proSum = [0] * n
        priSum = [0] * n
        modSum = [0] * n
        
        proSum[0] = strategy[0] * prices[0]
        priSum[0] = prices[0]
        
        for i in range(1, n):
            proSum[i] = proSum[i - 1] + strategy[i] * prices[i]
            priSum[i] = priSum[i - 1] + prices[i]
        
        for i in range(n - k + 1):
            if i == 0:
                left_pro = 0
                right_pro = proSum[n - 1] - proSum[k - 1]
            else:
                left_pro = proSum[i - 1]
                right_pro = proSum[n - 1] - proSum[i + k - 1]
            
            mid_start = i + k // 2
            mid_pri = priSum[i + k - 1] - (priSum[mid_start - 1] if mid_start > 0 else 0)
            
            modSum[i] = left_pro + mid_pri + right_pro
        
        return max(max(modSum[:n - k + 1]), proSum[n - 1])
