# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        
        def postorder(node):
            # Base case: Null node is a valid BST with sum 0.
            if not node:
                return True, float('inf'), float('-inf'), 0
            
            # Recursively check left and right subtrees.
            left_is_bst, left_min, left_max, left_sum = postorder(node.left)
            right_is_bst, right_min, right_max, right_sum = postorder(node.right)
            
            # If the current node is a valid BST:
            if left_is_bst and right_is_bst and left_max < node.val < right_min:
                # Calculate the sum of this subtree.
                subtree_sum = left_sum + right_sum + node.val
                # Update the maximum sum.
                self.max_sum = max(self.max_sum, subtree_sum)
                # Return True for BST validity, and update the min and max values for the current subtree.
                return True, min(node.val, left_min), max(node.val, right_max), subtree_sum
            else:
                # If not a BST, return False and sum 0.
                return False, 0, 0, 0
        
        self.max_sum = 0
        postorder(root)
        return self.max_sum
