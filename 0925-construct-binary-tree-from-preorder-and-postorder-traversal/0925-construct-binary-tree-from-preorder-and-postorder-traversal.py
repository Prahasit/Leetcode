# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        #second last element in postorder is start of right in preorder
        if not preorder or not postorder:
            return None

        root = TreeNode(preorder[0])
        
        if len(postorder) > 1:
            mid = preorder.index(postorder[-2])  # Second last element in postorder is the start of right in preorder
        else:
            mid = 1
        
        root.left = self.constructFromPrePost(preorder[1: mid], postorder[:mid - 1])
        root.right = self.constructFromPrePost(preorder[mid:], postorder[mid - 1:- 1])

        return root