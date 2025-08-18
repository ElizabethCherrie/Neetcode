"""Task 2 Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u_char = {}
        new_start = 0
        long_len = 0
        for i in range(len(s)):
            if s[i] in u_char:
                new_start = max(u_char[s[i]] + 1, new_start)
            u_char[s[i]] = i
            long_len = max(long_len, i - new_start + 1)
        return long_len