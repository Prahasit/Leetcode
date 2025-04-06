# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def solve(arr):
            if len(arr) == 0:
                return 
                
            root = TreeNode(max(arr))
            idx = arr.index(root.val)

            l = arr[:idx]
            r = arr[idx + 1:]

            root.left = solve(l)
            root.right = solve(r)

            return root

        return solve(nums)
        
