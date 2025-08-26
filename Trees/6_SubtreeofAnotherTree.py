"""Task 6 Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true 
if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. 
The tree tree could also be considered as a subtree of itself.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def diffinder(root, subroot):
            if root is None and subroot is None:
                return True
            if root is None or subroot is None:
                return False

            if root.val != subroot.val:
                return False
            left = diffinder(root.left, subroot.left)
            right = diffinder(root.right, subroot.right)

            return left and right

        if root is None:
            return False

        checker = diffinder(root, subRoot) 
        checker_l = self.isSubtree(root.left, subRoot) 
        checker_r = self.isSubtree(root.right, subRoot) 

        return checker or checker_l or checker_r
