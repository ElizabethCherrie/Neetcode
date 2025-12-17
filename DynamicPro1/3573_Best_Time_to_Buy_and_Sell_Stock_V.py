"""Task 3573. Best Time to Buy and Sell Stock V

You are given an integer array prices where prices[i] is the price of a stock in dollars on the ith day, and an integer k.

You are allowed to make at most k transactions, where each transaction can be either of the following:

Normal transaction: Buy on day i, then sell on a later day j where i < j. You profit prices[j] - prices[i].

Short selling transaction: Sell on day i, then buy back on a later day j where i < j. You profit prices[i] - prices[j].

Note that you must complete each transaction before starting another. Additionally, you can't buy or sell on the same day 
you are selling or buying back as part of a previous transaction.

Return the maximum total profit you can earn by making at most k transactions."""

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        def makeTransaction(dp: List[int])-> List[int]:
            update = [0] * n
            nrml, shrt = -prices[0], prices[0]

            for idx, price in (enumerate(prices[1:])):
                update[idx + 1] = max(update[idx], nrml + price, shrt - price)
                nrml, shrt = max(nrml, dp[idx] - price), max(shrt, dp[idx] + price)
            return update


        n = len(prices)
        dp = [0] * n

        for _ in range(k):
            dp = makeTransaction(dp)
        return dp[-1]        