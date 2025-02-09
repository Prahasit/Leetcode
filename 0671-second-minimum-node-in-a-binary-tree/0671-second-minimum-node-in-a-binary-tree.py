# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        #take all elemnts keep into array and return 2nd element
        result = []
        def dfs(node):

            if node is None:
                return

            result.append(node.val)
            left = dfs(node.left)
            right = dfs(node.right)

        dfs(root)
        result.sort()
        temp = result[0]
        for i in range(1, len(result)):
            if result[i] != temp:
                return result[i]

        return - 1

        