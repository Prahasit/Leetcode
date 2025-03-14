# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(node, minval, maxval):
            if node is None:
                return True

            if node.val <= minval or node.val >= maxval:
                return False
            return solve(node.left, minval, node.val) and solve(node.right, node.val, maxval)

            
        return solve(root, float('-inf'), float('inf'))

            


        
        