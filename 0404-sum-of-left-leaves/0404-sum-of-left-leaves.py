# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_sum = 0
        def dfs(root):
            nonlocal left_sum
            if root is None:
                return 0

            if root.left is None and root.right is None:
                return root.val

            temp = dfs(root.left)
            left_sum += temp
            dfs(root.right)

            return 0
            
        dfs(root)
        return left_sum





        

        