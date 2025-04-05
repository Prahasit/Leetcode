# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def solve(node, total_val):
            if node is None:
                return 0
            
            total_val = total_val * 10 + node.val

            if node.left is None and node.right is None:
                return total_val

            left = solve(node.left, total_val)
            right = solve(node.right, total_val)

            return left + right

        
        return solve(root, 0)