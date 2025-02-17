# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        q = deque()
        q.append(root)
        level = 0

        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level % 2 == 1:
                l, r = 0, len(temp) - 1
                while l < r:
                    temp[l].val, temp[r].val = temp[r].val, temp[l].val
                    l += 1
                    r -= 1
            level += 1
        return root
