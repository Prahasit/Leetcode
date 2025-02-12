# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        unival =True
        prev = None
        def dfs(node):
            nonlocal prev, unival
            if node is None:
                return
            dfs(node.left)
            if prev is not None and prev != node.val:
                unival = False
            prev = node.val #updating prev to current node value if it is None
            dfs(node.right)
        
    

        dfs(root)
        return unival
        
