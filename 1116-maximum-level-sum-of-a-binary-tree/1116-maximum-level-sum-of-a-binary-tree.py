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
        level = 0
        max_sum = float('-inf')
        ans_level = 1
        q = deque()
        q.append(root)

        while q:
            level += 1
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()

                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                ans_level = level

        return ans_level



