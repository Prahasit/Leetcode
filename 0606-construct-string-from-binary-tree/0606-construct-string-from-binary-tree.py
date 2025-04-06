# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        def solve(node):
            if node is None:
                return

            res.append("(")
            res.append(str(node.val))

            if node.left is None and node.right:
                res.append("()")

            solve(node.left)
            solve(node.right)

            res.append(")")

        solve(root)

        return "".join(res)[1: - 1]
