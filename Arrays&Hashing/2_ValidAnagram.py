""" Task2 Valid Anagram
Given two strings s and t, return true if the two strings are 
anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters 
as another string, but the order of the characters can be different."""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)