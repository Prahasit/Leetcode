# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal is in sorted order.
        # so get inorder and get the kth smaller

        result = []
        def inorder(node):
            
            if node is None:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        return result[k - 1]