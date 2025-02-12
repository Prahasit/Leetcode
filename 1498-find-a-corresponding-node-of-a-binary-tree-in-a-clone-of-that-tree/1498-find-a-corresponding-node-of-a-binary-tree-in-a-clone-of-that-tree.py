# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def inorder(node, clone):
            if node is None:
                return
            inorder(node.left, clone.left)
            if node.val == target.val:
                self.res = clone
            inorder(node.right, clone.right)

        inorder(original, cloned)
        return self.res
        