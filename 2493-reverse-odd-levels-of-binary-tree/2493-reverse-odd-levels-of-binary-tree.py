# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(left_node, right_node, level):
            if left_node is None or right_node is None:
                return
            if level % 2 ==0:
                left_node.val, right_node.val = right_node.val, left_node.val

            dfs(left_node.left, right_node.right, level + 1)
            dfs(left_node.right, right_node.left, level + 1)
        dfs(root.left, root.right, 0)
        return root
