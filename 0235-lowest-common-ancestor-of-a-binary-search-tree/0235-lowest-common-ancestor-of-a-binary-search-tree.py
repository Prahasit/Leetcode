# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(node):
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                return node

            if node.val < p.val and node.val < q.val:
                return solve(node.right)
            elif node.val > p.val and node.val > q.val:
                return solve(node.left)

           
        return solve(root)