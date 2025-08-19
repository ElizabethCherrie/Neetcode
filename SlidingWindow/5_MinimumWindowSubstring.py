"""Task 5 Minimum Window Substring
Given two strings s and t, return the shortest substring of s such that
every character in t, including duplicates, is present in the substring.
If such a substring does not exist, return an empty string "".
You may assume that the correct output is always unique."""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        char_c = {}
        for char in t:
            char_c[char] = char_c.get(char, 0) + 1

        char_win = {}
        l = 0
        matchy = 0
        min_len = len(s) + 1
        min_win = ""

        for r in range(len(s)):
            char_win[s[r]] = 1 + char_win.get(s[r], 0)

            if s[r] in char_c and char_win[s[r]] == char_c[s[r]]:
                matchy += 1

            while l <= r and matchy == len(char_c):
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_win = s[l:r+1]
                char_win[s[l]] -= 1
                if s[l] in char_c and char_win[s[l]] < char_c[s[l]]:
                    matchy -= 1
                l += 1

        return min_win