# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        #taking left = 0 and right = 0
        result = 0
        def dfs(node, prev, steps):
            nonlocal result
            if node is None:
                return None

            result = max(result, steps)

            if prev == 0: 
                dfs(node.right, 1, steps + 1)
                dfs(node.left, 0, 1) #starting new path

            else:
                dfs(node.left, 0, steps + 1)
                dfs(node.right, 1, 1) #starting new path

        dfs(root, 0, 0)
        return result