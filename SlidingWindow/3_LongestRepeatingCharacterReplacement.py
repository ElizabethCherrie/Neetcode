"""Task 3 Longest Repeating Character Replacement
You are given a string s consisting of only uppercase english characters 
and an integer k. You can choose up to k characters of the string and 
replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest
 substring which contains only one distinct character.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        u_char_c = {}
        l = 0
        longest = 0
        max_c = 0

        for r in range(len(s)):
            u_char_c[s[r]] = 1 + u_char_c.get(s[r], 0)
            max_c = max(max_c, u_char_c[s[r]])
            if (r - l + 1) - max_c > k:
                u_char_c[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest