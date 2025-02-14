# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, min_val, max_val):
            nonlocal res
            if node is None:
                return 
            res = max(res, abs(min_val - node.val), abs(max_val - node.val))
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)

            dfs(node.left, min_val, max_val)
            dfs(node.right, min_val, max_val)

        dfs(root, root.val, root.val)
        return res