# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        memo = {}
        def generate(start, end):

            if (start, end) in memo:
                return memo[(start, end)]

            all_trees = []
            if start > end:
                all_trees.append(None)
                return all_trees

            for i in range(start, end + 1):
                # i is the root
                left_tree = generate(start, i - 1)
                right_tree = generate(i + 1, end)


                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(i, left, right)
                        all_trees.append(root)
                        
            memo[(start, end)] = all_trees
            return all_trees

        return generate(1, n)






        