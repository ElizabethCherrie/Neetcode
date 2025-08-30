"""Task 13 Construct Binary Tree from Preorder and Inorder Traversal
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
   
        def recurse(preorder, inorder):

            if not preorder or not inorder:
                return None

            root_val = preorder[0]
            node = TreeNode(root_val)
            index = inorder.index(root_val)

            left_inorder = inorder[:index]
            right_inorder = inorder[index+1:]
            left_preorder = preorder[1 : 1+len(left_inorder)]
            right_preorder = preorder[1+len(left_inorder) : ]

            node.left = recurse(left_preorder, left_inorder)
            node.right = recurse(right_preorder, right_inorder)
            
            return node

        return recurse(preorder, inorder)