"""Task 6 Copy Linked List with Random Pointer
You are given the head of a linked list of length n. Unlike a singly linked list,
each node contains an additional pointer random, which may point to any node in the list, or null.
Create a deep copy of the list.
The deep copy should consist of exactly n new nodes, each including:
The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.
Return the head of the copied linked list.
In the examples, the linked list is represented as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where random_index is the index 
of the node (0-indexed) that the random pointer points to, or null if it does not point to any node."""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cop = {None:None}
        new_head = head

        while new_head:
            copy = Node(new_head.val)
            cop[new_head] = copy
            new_head = new_head.next

        new_head2 = head
        while new_head2:
            copy2 = cop[new_head2]
            copy2.next = cop[new_head2.next]
            copy2.random = cop[new_head2.random]
            new_head2 = new_head2.next

        return cop[head]