# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        l = 0
        q = deque()
        q.append((root, -1, 0)) #node, parent, level

        while q:
            for _ in range(len(q)):
                node, par, level = q.popleft()

                if x == node.val:
                    temp1 = level
                    parent1 = par
                if y == node.val:
                    temp2 = level
                    parent2 = par
                if node.left:
                    q.append((node.left, node, level + 1))
                
                if node.right:
                    q.append((node.right, node, level + 1))

                
        return (temp1 == temp2 and parent1 != parent2)
