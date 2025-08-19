"""Task 4 Permutation in String
You are given two strings s1 and s2.
Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, then return true.
Both strings only contain lowercase letters."""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_c = {}
        char_c2 = {}
        if len(s1) > len(s2):
            return False
        for char in s1:
            char_c[char] = 1 + char_c.get(char, 0)
        l = 0
        for r in range(len(s2)):
            char_c2[s2[r]] = 1 + char_c2.get(s2[r], 0)
            if r - l + 1 > len(s1):
                char_c2[s2[l]] -= 1
                if char_c2[s2[l]] == 0:
                    del char_c2[s2[l]]
                l += 1
            if char_c2 == char_c:
                return True
        return False