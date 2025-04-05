# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res
        def solve(node):
            if node is None:
                return 0

            left = solve(node.left)
            right = solve(node.right)
            value = node.val + left + right
            freq[value] += 1
            return value
        
        freq = defaultdict(int)
        solve(root)

        max_freq = max(freq.values())
        for key, val in freq.items():
            if val == max_freq:
                res.append(key)
        
        return res

