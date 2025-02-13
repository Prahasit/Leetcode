# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if node is None:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.left is None and node.right is None and node.val == 0:
                return None

            return node

        return dfs(root)