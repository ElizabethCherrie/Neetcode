"""Task 8 Binary Tree Level Order Traversal
Given a binary tree root, return the level order traversal of it as a nested list, 
where each sublist contains the values of nodes at a particular level in the tree, from left to right.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 1)])
        cur_depth = 1
        level = []
        result = []
        while q:
            node, depth = q.popleft()

            if node.left:
                q.append((node.left, depth + 1))

            if node.right:
                q.append((node.right, depth + 1))

            if cur_depth == depth:
                level.append(node.val)

            elif cur_depth < depth:
                result.append(level)
                cur_depth = depth
                level = [node.val]
        
        result.append(level)

        return result