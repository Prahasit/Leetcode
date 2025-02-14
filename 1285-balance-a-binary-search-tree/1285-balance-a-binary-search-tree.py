# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # convert into array using inorder traversal
        res = []
        def inorder(node):
            if node is None:
                return 

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)

        def balance(res, start, end):
            if start > end:
                return
            mid = (start + end) //2
            left_tree = balance(res, start, mid - 1)
            right_tree = balance(res, mid + 1, end)

            node = TreeNode(res[mid], left_tree, right_tree)

            return node

        return balance(res, 0, len(res) - 1)



            