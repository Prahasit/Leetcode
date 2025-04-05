# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        prev = None
        unival =True
        def solve(node):
            nonlocal prev, unival
            if node is None:
                return 

            solve(node.left)
            if prev is not None and prev != node.val:
                unival = False
            prev = node.val
            solve(node.right)

        solve(root)
        return unival