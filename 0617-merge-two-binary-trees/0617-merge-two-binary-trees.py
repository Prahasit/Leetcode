# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def solve(node1, node2):
            if not node1 and not node2:
                return None
            
            v1 = node1.val if node1 else 0
            v2 = node2.val if node2 else 0

            root = TreeNode(v1 + v2)
            root.left = solve(node1.left if node1 else None, node2.left if node2 else None)
            root.right = solve(node1.right if node1 else None, node2.right if node2 else None)

            return root

            
        return solve(root1, root2)
        


        