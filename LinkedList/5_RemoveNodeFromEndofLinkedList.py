"""Task 5 Remove Node From End of Linked List
You are given the beginning of a linked list head, and an integer n.
Remove the nth node from the end of the list and return the beginning of the list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gap = head
        delete = dummy

        for i in range(n):
            gap = gap.next
        
        while gap:
            delete = delete.next
            gap = gap.next
        
        delete.next = delete.next.next
        return dummy.next