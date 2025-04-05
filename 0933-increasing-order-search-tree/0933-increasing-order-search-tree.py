# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root_node = TreeNode()
        new_node = root_node

        def solve(node):
            nonlocal root_node
            if node is None:
                return
            solve(node.left)

            root_node.right = TreeNode(node.val)
            root_node = root_node.right

            solve(node.right)

        solve(root)
        return new_node.right