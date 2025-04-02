# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        #preorder is root first
        if not preorder:
            return
        root = TreeNode(preorder[0])
        low = [i for i in preorder if i < preorder[0]]
        high = [i for i in preorder if i > preorder[0]]
        
        
        root.left = self.bstFromPreorder(low)
        root.right = self.bstFromPreorder(high)

        return root


