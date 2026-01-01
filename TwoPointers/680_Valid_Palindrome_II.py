"""Task 680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPolindrom(l, r):
            diff = 0

            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        l, r = 0, len(s) - 1
  
        while l < r:

            if s[l] != s[r]:
                return (isPolindrom(l + 1, r) or isPolindrom(l, r - 1))
                
            l += 1
            r -= 1
        
        return True