# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if node is None:
                return 0
            
            left = solve(node.left)
            right = solve(node.right)

            if abs(left - right ) > 1 or left < 0 or right < 0:
                return -1
            
            return 1 + max(left, right)

        return solve(root) >= 0