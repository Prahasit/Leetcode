# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        def dfs(node, temp):
            if node is None:
                return
            temp += str(node.val)
            if node.left is None and node.right is None:
                result.append(temp)

            else:
                dfs(node.left, temp + '->')
                dfs(node.right, temp + '->')
        

        dfs(root, '')
        return result