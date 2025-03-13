# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(node):
            if node is None:
                return

            left = solve(node.left)
            right = solve(node.right)

            node.left, node.right = right, left

            return node

        solve(root)
        return root
