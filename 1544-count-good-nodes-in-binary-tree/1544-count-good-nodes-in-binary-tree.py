# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(node, minval, maxval):
            nonlocal count
            if node is None:
                return

            if node.val >= maxval and node.val >= minval:
                count += 1
            minval = min(minval, node.val)
            maxval = max(maxval, node.val)

            solve(node.left, minval, maxval)
            solve(node.right, minval, maxval)

        count = 0
        solve(root, root.val, root.val)
        return count