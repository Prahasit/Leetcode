"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        def dfs(node):
            if node is None:
                return
            result.append(node.val)
            for i in node.children:
                dfs(i)
        dfs(root)

        return result
        


        

        