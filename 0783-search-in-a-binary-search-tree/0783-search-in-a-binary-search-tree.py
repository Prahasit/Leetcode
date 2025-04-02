# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def solve(node):
            if node is None:
                return node
            if val == node.val:
                return node
            elif val > node.val:
                return solve(node.right)
            
            else:
                return solve(node.left)


        return solve(root)
        