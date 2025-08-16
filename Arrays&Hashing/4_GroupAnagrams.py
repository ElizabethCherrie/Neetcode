"""Task 4 Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. 
You may return the output in any order.An anagram is a string that contains the 
exact same characters as another string, but the order of the characters can be different.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        sor = []
        for i in strs:
            a = "".join(sorted(i))
            res[a].append(i)
        
        return list(res.values())