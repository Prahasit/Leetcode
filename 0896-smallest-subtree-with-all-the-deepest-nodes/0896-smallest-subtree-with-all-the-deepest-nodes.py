# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return 0, None
            
            left, left_node = dfs(node.left)
            right, right_node  = dfs(node.right)

            if left == right:
                return left + 1, node
            if left > right:
                return left + 1, left_node
            if left < right:
                return right + 1, right_node

        dist, node = dfs(root)
        return node
        