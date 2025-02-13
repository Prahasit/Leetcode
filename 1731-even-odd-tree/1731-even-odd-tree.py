# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        res = []
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

            if len(res) % 2 == 0:
                for i in range(len(level)):
                    if level[i - 1] % 2 == 0:
                        return False
                    if i > 0 and level[i] <= level[i - 1]:
                        return False
                res.append(level)
                
            else:
                for i in range(len(level)):
                    if level[i - 1] % 2 != 0:
                        return False
                    if  i > 0 and level[i] >= level[i - 1]:
                        return False
                res.append(level)
            
        return True


        