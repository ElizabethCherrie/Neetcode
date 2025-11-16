"""Task 1513. Number of Substrings With Only 1s

Given a binary string s, return the number of substrings with all characters 1's. 
Since the answer may be too large, return it modulo 109 + 7.
"""

class Solution:
    def numSub(self, s: str) -> int:
        cnt = 0
        for part in s.split('0'):
            n = len(part)
            cnt += n*(n+1)

        return (cnt // 2) % (10**9 + 7)