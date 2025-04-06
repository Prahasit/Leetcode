# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def solve(node1, node2):
            if node1 is None and node2 is None:
                return True
                
            if node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False

            no_swap = solve(node1.left, node2.left) and solve(node1.right, node2.right)

            swap = solve(node1.left, node2.right) and solve(node1.right, node2.left)

            return swap or no_swap

        return solve(root1, root2)
        