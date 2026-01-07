"""Task 1339. Maximum Product of Splitted Binary Tree

Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
                
        def dfs(node):
            l = 0
            if node.left:
                l = dfs(node.left) 
            
            r = 0
            if node.right:
                r = dfs(node.right)

            node.val = r + l + node.val
            
            return node.val
        
        def utka(node):
            s = node.val * (root.val - node.val)
            
            lm = 0
            if node.left:
                lm = utka(node.left)
                
            rm = 0
            if node.right:
                rm = utka(node.right)
            
            return max(rm, lm, s)
            
        dfs(root)
        
        return utka(root) % MOD