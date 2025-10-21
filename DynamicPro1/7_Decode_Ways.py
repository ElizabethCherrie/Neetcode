"""Task7 Decode Ways
A string consisting of uppercase english characters can be encoded to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above. 
There may be multiple ways to decode a message. For example, "1012" can be mapped into:

"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)
The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it. You can assume that the answer fits
in a 32-bit integer.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        prev_ways = 1 
        curr_ways = 1

        for i in range(1, len(s)):
            prev = int(s[i - 1])
            curr = int(s[i])
            two_digit = prev * 10 + curr

            ways = 0 

            if curr == 0 and (prev != 1 and prev != 2):
                return 0

            if curr != 0:
                ways += curr_ways

            if 10 <= two_digit <= 26:
                ways += prev_ways

            prev_ways, curr_ways = curr_ways, ways

        return curr_ways