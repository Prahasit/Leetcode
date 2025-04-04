# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def solve(node):
            nonlocal target

            if node is None:
                return
            if low <= node.val <= high:
                target += node.val

            solve(node.left)
            solve(node.right)
            
        target = 0
        solve(root)

        return target