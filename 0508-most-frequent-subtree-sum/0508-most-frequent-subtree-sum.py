# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        hashmap = defaultdict(int)
        result = []
        if root is None:
            return []
        def dfs(node):

            if node is None:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            cur_sum = left_sum + right_sum + node.val # the value of node is leftsubree + right subtree + its value
            hashmap[cur_sum] += 1
            return cur_sum
            

        dfs(root)
        max_freq = max(hashmap.values())
        
        for key, val in hashmap.items():
            if val == max_freq:
                result.append(key)
        return result


