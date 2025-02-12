# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root_node = TreeNode()
        new_tree = root_node
        def dfs(node):
            nonlocal root_node
            if node is None:
                return

            dfs(node.left)
            root_node.right = TreeNode(node.val)
            root_node = root_node.right
            dfs(node.right)

        dfs(root)
        return new_tree.right
