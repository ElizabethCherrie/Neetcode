"""Task 3 Diameter of Binary Tree
The diameter of a binary tree is defined as the length of the longest path 
between any two nodes within the tree.
The path does not necessarily have to pass through the root.
The length of a path between two nodes in a binary tree is the number of edges
between the nodes. Note that the path can not include the same node twice.
Given the root of a binary tree root, return the diameter of the tree."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def further(root):
            if not root:
                return 0
            left = further(root.left)
            right = further(root.right)
            self.res = max(self.res, left + right)

            return 1 + max(left, right)
        
        further(root)
        return self.res