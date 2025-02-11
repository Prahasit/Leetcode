# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = []
        def dfs(node, bin_str):
            if node is None:
                return
            if node.left is None and node.right is None:
                bin_str = bin_str + str(node.val)
                result.append(int(bin_str, 2)) # converting binary string to decimal
            dfs(node.left, bin_str + str(node.val))
            dfs(node.right, bin_str + str(node.val))

        dfs(root, "")
        return sum(result)
        