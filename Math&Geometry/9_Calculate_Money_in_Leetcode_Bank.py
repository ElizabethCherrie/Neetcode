"""Task 9 Calculate Money in Leetcode Bank
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in
$1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.
"""

class Solution:
    def totalMoney(self, n: int) -> int:
        week = 0 
        total = 0
        day = 1
        
        for i in range(n):
            if day == 8:
                day = 1
                week += 1
            
            total += day + week
            
            day += 1    
            
        return total