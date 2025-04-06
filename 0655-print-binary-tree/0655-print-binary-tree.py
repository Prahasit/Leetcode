# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getHeight(node):
            if not node:
                return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        level = getHeight(root)
        row = level
        col = 2 ** level - 1

        result = [[""] * col for _ in range(row)]
        
        def solve(node, r, c):
            if node is None:
                return

            result[r][c] = str(node.val)
            gap = 2 ** (level - r - 2)

            if node.left:
                solve(node.left, r + 1, c - gap)

            if node.right:
                solve(node.right, r + 1, c + gap)


        solve(root, 0, (col - 1 )// 2)
        return result
