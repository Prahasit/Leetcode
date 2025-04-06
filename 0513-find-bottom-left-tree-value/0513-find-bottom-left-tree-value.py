# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return
        
        q = deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

                left_level = node.val

        return left_level