"""Task 7 Palindrome Partitioning 
Given a string s, split s into substrings where every substring is a palindrome. 
Return all possible lists of palindromic substrings.
You may return the solution in any order."""

class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        poli = []

        def dfs(i):
            if i >= len(s):
                res.append(poli.copy())
                return

            for j in range(i, len(s)):
                if checker(s, i, j):
                    poli.append(s[i:j + 1:])
                    dfs(j + 1)
                    poli.pop()

        def checker(word, l, r):
            while l < r:
                if word[l] != word[r]:
                    return False

                l, r = l + 1, r - 1
            return True

        dfs(0)
        return res 