# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []

        def solve(node, res):
            if node is None:
                return 

            if node.left is None and node.right is None:
                res.append(node.val)

            solve(node.left, res)
            solve(node.right, res)

        solve(root1, res1)
        solve(root2, res2)

        return res1 == res2

