"""Task 12 Kth Smallest Integer in BST
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = 0

        def small_k(node, target):

            nonlocal count

            if not node:
                return None

            left_small = small_k(node.left, target)

            if left_small is not None:
                return left_small

            count += 1

            if count == target:
                return node.val
            
            right_small = small_k(node.right, target)
            return right_small

        return small_k(root, k)