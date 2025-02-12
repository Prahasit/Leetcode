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
        result = []
        while q:
            level += 1
            l = []
            for _ in range(len(q)):
                node = q.popleft() 
                if len(result) == level - 1:
                    result.append(node.val)
            
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)        
            

        return result