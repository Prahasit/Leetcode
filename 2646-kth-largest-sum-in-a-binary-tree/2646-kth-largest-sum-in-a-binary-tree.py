# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        if root is None:
            return
        q = deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            temp = sum(level)
            res.append(temp)

        res.sort()
        return res[len(res) - k] if k <= len(res) else - 1



