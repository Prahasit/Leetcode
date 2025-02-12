# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # first take all the paths and save it into an array or list
        #then traverse the array and find lexographicaaly shortest 

        result = []
        def dfs(node, temp_str):
            if node is None:
                return

            
            if node.left is None and node.right is None:
                temp_str = chr(ord('a') +  node.val) + temp_str
                result.append(temp_str)

            dfs(node.left, chr(ord('a') +  node.val) +temp_str )
            dfs(node.right, chr(ord('a') +  node.val) +temp_str)


        dfs(root, "")
        result.sort()
        return result[0]
        