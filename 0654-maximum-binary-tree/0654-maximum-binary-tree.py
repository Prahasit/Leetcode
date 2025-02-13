# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(temp):
            if len(temp) == 0:
                return
            
            root = TreeNode(max(temp))
            idx = temp.index(max(temp))
            root.left = dfs(temp[: idx])
            root.right = dfs(temp[idx + 1:])

            return root


        return dfs(nums)
