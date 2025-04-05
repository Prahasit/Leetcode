# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val % 2  == 0:
            return False
        q = deque()
        q.append((root, 0))
        result = []

        while q:
            l = []
            for _ in range(len(q)):
                node, level = q.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 1:
                        if len(l) == 0 or node.val > l[-1]:
                            l.append(node.val)
                        else:
                            return False
                    else:
                        return False

                else:
                    if node.val % 2 == 0:
                        if len(l) == 0 or node.val < l[-1]:
                            l.append(node.val)
                        else:
                            return False
                    else:
                        return False

                
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
            print(l)   
            result.append(l)
        return True



        