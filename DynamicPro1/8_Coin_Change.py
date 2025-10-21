"""Task 8 Coin Change
You are given an integer array coins representing coins of different denominations 
(e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount. 
If it is impossible to make up the amount, return -1.

You may assume that you have an unlimited number of each coin."""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minList = {}

        def dfs(amount):
            res = 1e9

            if amount == 0:
                return 0

            if amount in minList:
                return minList[amount]

            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            minList[amount] = res

            return res

        minAm = dfs(amount)
        
        return -1 if minAm == 1e9 else minAm