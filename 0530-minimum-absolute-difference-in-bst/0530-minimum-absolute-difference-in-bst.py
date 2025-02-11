# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        #as inorder of BST is in sorted order
        min_val = float('inf')
        result = []
        def dfs(node):

            if node is None:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)

        for i in range(1, len(result)):
            min_val = min(min_val, result[i] - result[i - 1])

        return min_val


        