# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            nonlocal res
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            left_val, right_val = 0, 0
            if node.left and node.left.val == node.val:
                left_val = 1 + left
            
            if node.right and node.right.val == node.val:
                right_val = 1 + right
            
            res = max(res, left_val + right_val)

            return max(left_val, right_val)


        res = 0
        dfs(root)
        return res
        