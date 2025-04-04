# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if not node.left and not node.right:
                return bool(node.val)  # leaf node (0 or 1)
            
            left_val = solve(node.left)
            right_val = solve(node.right)

            if node.val == 2:
                return left_val or right_val
            elif node.val == 3:
                return left_val and right_val

        return solve(root)