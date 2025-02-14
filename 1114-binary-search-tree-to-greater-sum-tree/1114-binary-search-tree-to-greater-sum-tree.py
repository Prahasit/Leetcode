# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #doing reverse inorder 
        res = []
        cur_sum = 0
        def rev_inorder(node):
            nonlocal cur_sum
            if node is None:
                return
            
            rev_inorder(node.right)
            cur_sum += node.val
            node.val = cur_sum
            rev_inorder(node.left)
            
        rev_inorder(root)
        return root
            

        
