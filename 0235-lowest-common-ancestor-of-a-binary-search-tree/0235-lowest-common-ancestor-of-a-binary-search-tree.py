# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def solve(node, p ,q):
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                return node
            
            if node.val > p.val and node.val > q.val:
                return solve(node.left, p, q)
            if node.val < p.val and node.val < q.val:
                return solve(node.right, p, q)
        
        return solve(root, p, q)
         

        