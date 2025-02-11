from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_sum = 0

        def dfs(node, is_left):
            nonlocal left_sum
            if node is None:
                return

            # If it's a left leaf, add its value
            if is_left and node.left is None and node.right is None:
                left_sum += node.val
                return

            # Recursively process left and right children
            dfs(node.left, True)
            dfs(node.right, False)

        dfs(root, False)
        return left_sum
