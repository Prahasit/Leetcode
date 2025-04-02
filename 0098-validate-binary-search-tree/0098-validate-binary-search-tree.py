# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def explore(node, minval, maxval):
            if node is None:
                return True
            if node.val <= minval or node.val >= maxval:
                return False
            
            return  explore(node.left, minval, node.val) and explore(node.right, node.val, maxval)
            
        
        return explore(root, float('-inf'), float('inf'))