"""Task 8 Letter Combinations of a Phone Number
You are given a string digits made up of digits from 2 through 9 inclusive.
Each digit (not including 1) is mapped to a set of characters as shown below:
A digit could represent any one of the characters it maps to.
Return all possible letter combinations that digits could represent. You may return the answer in any order."""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        res = [""]

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        for each in digits:
            comb = []

            for letter in res:
                for c in digitToChar[each]:
                    comb.append(letter + c)
                    
            res = comb

        return res