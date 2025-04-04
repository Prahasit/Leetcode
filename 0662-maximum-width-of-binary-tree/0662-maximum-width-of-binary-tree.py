# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        left_pos = {}
        def solve(node, depth, index):
            if node is None:
                return 0

            if depth not in left_pos:
                left_pos[depth] = index


            cur_width = index - left_pos[depth] + 1

            left_width = solve(node.left, depth + 1, 2 * index)
            right_width = solve(node.right, depth+ 1, 2 * index + 1)

            return max(cur_width, left_width, right_width)

        return solve(root, 0, 1)
