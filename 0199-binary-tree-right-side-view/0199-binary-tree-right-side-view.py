# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        level = 0
        res =[]
        while q:
            level += 1
            for _ in range(len(q)):
                node = q.popleft()
                if len(res) == level - 1:
                    res.append(node.val)
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)


        return res 



        