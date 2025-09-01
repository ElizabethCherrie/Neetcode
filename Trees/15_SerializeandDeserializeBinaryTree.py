"""Task 14 Serialize and Deserialize Binary Tree
mplement an algorithm to serialize and deserialize a binary tree.
Serialization is the process of converting an in-memory structure into
a sequence of bits so that it can be stored or sent across a network to be
reconstructed later in another computer environment.
You just need to ensure that a binary tree can be serialized to a string and 
this string can be deserialized to the original tree structure.
There is no additional restriction on how your serialization/deserialization algorithm should work.
Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. 
You do not necessarily need to follow this format.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(node):
            if not node:
                result.append("null")
                return
            result.append(str(node.val))

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = iter(data.split(","))

        def dfs():

            val = next(values)

            if val == "null":
                return None

            node = TreeNode(int(val))

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()