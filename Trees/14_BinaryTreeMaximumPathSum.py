"""Task 14 Binary Tree Maximum Path Sum
Given the root of a non-empty binary tree, return the maximum path sum of any non-empty path.
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them.
A node can not appear in the sequence more than once. The path does not necessarily need to include the root.
The path sum of a path is the sum of the node's values in the path."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        final_max = [root.val]

        def dfs(root):
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            final_max[0] = max(final_max[0], root.val + left + right)

            return root.val + max(left, right)
        
        dfs(root)
        return final_max[0]