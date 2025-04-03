# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            nonlocal diameter
            if node is None:
                return 0
            
            left = solve(node.left)
            right = solve(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        
        diameter = 0
        solve(root)

        return diameter