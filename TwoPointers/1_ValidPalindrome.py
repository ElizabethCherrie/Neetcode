"""Task 1 Valid Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_s = ""
        for i in s:
            if i.isalnum():
                lower_s += i.lower()

        r = len(lower_s) - 1
        for l in range(len(lower_s) // 2):
            if lower_s[l] != lower_s[r-l]:
                return False
        return True
