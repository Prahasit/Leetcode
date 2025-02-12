# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        q = deque()
        q.append(root)
        level = 0
        max_level_sum = float('-inf')
        max_level = 0
        while q:
            level_sum = 0
            level += 1
            for i in range(len(q)):
                node = q.popleft()

                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = level

        return max_level

        