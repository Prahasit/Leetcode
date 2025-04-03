# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            nonlocal max_path
            if node is None:
                return 0
            left = solve(node.left)
            right = solve(node.right)
            #assign 0 if left or right is 0 as we should not consider
            if left < 0:
                left = 0
            if right < 0:
                right = 0

#at every node we need to check for max so checking node + left + right
            max_path = max(max_path, node.val + left + right)
            return node.val + max(left, right)

        max_path = float('-inf')
        solve(root)
        return max_path