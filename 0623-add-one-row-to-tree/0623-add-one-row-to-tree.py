# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def dfs(node, curr_depth):
            if node is None:
                return

            if curr_depth == depth - 1:
                temp_left, temp_right = node.left, node.right
                node.left = TreeNode(val)
                node.right = TreeNode(val)

                node.left.left = temp_left
                node.right.right = temp_right

                return root


            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)
            return root


        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        return dfs(root, 1)




        
        