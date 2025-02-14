# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        # do inroder traversal as it is BST and it will be in ordered order
        # for queries find the ceil and floor of that number using Binary Search
        res = []
        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)

        answer = []
        for q in queries:
            l, r = 0, len(res) - 1
            mini, maxi = -1, -1
            
            while l <= r:
                mid = (l + r) // 2
                if q <= res[mid]:
                    r = mid - 1
                    maxi = res[mid]
                else:
                    l = mid + 1

            l, r = 0, len(res) - 1
            while l <= r:
                mid = (l + r) // 2
                if q >= res[mid]:
                    mini = res[mid]
                    l = mid + 1
                else:
                    r = mid - 1

            answer.append([mini, maxi])
        return answer
                






        