# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        '''There are three cases for distributing coins from a leaf node:

The leaf node doesn't have any coins: Take a coin from the parent, since the parent is the only node it is connected to.
The leaf node has exactly one coin: No coins need to be exchanged.
The leaf node has more than one coin: Keep one coin and give all the extra coins to the parent.
        '''
        def dfs(node):
            nonlocal moves
            if node is None:
                return 0
            
            leftcoins = dfs(node.left)
            rightcoins = dfs(node.right)

            moves += abs(leftcoins) + abs(rightcoins)

            return node.val - 1 + leftcoins + rightcoins



        moves = 0
        dfs(root)
        return moves