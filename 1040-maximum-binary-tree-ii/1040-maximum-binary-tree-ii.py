# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if node is None:
                return TreeNode(val)

            if val > node.val:
                new_node = TreeNode(val)
                new_node.left = node
                return new_node
            node.right = dfs(node.right)

            return node

        return dfs(root)
        