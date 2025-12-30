"""Task 705. Design HashSet

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""

class MyHashSet:

    def __init__(self):
        self.hashSet = []

    def add(self, key: int) -> None:
        if key not in self.hashSet:
            self.hashSet.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashSet:
            self.hashSet.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.hashSet:
            return True
        return False
