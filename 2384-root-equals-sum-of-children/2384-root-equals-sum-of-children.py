# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if node.val == node.left.val + node.right.val:
                return True
            else:
                return False

        return solve(root)
            