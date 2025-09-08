"""Task 2 Design Add and Search Word Data Structure
Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure
that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter."""

class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["end"] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return "end" in node
            char = word[i]
            if char == ".":
                for key, child in node.items():
                    if key != "end" and dfs(child, i + 1):
                        return True
            if char not in node:
                return False
            return dfs(node[char], i + 1)
        return dfs(self.root, 0)   