# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deepestLevel = 0
        currSum = 0

        def dfs(root,level):
            nonlocal deepestLevel,currSum
            if not root:
                return 

            if level==deepestLevel:
                currSum+=root.val
            elif level>deepestLevel:
                deepestLevel = level
                currSum = root.val
            
            dfs(root.left,level+1)
            dfs(root.right,level+1)

        dfs(root,0)
        return currSum