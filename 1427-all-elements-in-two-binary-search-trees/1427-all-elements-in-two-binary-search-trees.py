# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        res1, res2 = [], []
        def inorder(node, res):
            if node is None:
                return
            inorder(node.left,res)
            res.append(node.val)
            inorder(node.right,res)

        
            
        inorder(root1, res1)
        inorder(root2, res2)

        
        return sorted(res1 + res2)