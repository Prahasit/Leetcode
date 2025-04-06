"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def solve(node):
            if node is None:
                return
            
            for i in node.children:
                solve(i)
            
            res.append(node.val)
        
        solve(root)

        return res