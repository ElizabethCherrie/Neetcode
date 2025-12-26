"""Task 2483. Minimum Penalty for a Shop
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
"""

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y = [1 if customers[-1] == "Y" else 0]
        n = [1 if customers[0] == "N" else 0]
        
        for c in customers[1:]:
            if c == "N":
                n.append(n[-1] + 1)
            else:
                n.append(n[-1])
        
        for c in range(len(customers) - 2, -1, -1):
            if customers[c] == "Y":
                y.append(y[-1] + 1)
            else:
                y.append(y[-1])
        
        y.reverse()
        
        y.append(0)
        n = [0] + n
        m = 0
        
        mini = float('inf')
        for i in range(len(y)):
            if n[i] + y[i] < mini:
                m = i
                mini = n[i] + y[i]
        return m