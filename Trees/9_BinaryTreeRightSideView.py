"""Task 9 Binary Tree Right Side View
You are given the root of a binary tree. Return only the values of the nodes
that are visible from the right side of the tree, ordered from top to bottom."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        rightSide = []
        q = deque([root])
        full_l = 1

        while q:
            node = q.popleft()
            full_l -= 1

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            if not full_l:
                rightSide.append(node.val)
                full_l = len(q)

        return rightSide