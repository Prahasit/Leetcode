# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.res = set()

        self.root.val = 0
        def solve(node):
            if node is None:
                return 
            
            self.res.add(node.val)

            if node.left is not None:
                node.left.val = node.val * 2  + 1
                solve(node.left)
            if node.right is not None:
                node.right.val = node.val * 2  + 2
                solve(node.right)
            
        solve(self.root)

    def find(self, target: int) -> bool:
        
        if target in self.res:
            return True
        else:
            return False
            
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)