"""Task 4 Balanced Binary Tree
Given a binary tree, return true if it is height-balanced and false otherwise.
A height-balanced binary tree is defined as a binary tree in which the left and right 
subtrees of every node differ in height by no more than 1.
"""

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def depths(root):
            if root is None:
                return 0
            left = depths(root.left)
            right = depths(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return depths(root) != -1