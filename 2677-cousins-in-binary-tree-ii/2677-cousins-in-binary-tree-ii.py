# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #no to traverse two times--> once to get the sum at the level --> 2nd tie to substract the level sum - sum of siblings of that node


        res = []
        q = deque()
        q.append(root)

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()

                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level_sum)
        print(res)
        root.val = 0 # it doesn have any cousins
        level = 0
        q.append(root)

        while q:
            level += 1 
            for _ in range(len(q)):
                node = q.popleft()

                if node.left and node.right:
                    temp1 = node.left.val
                    temp2 = node.right.val
                    node.left.val = res[level] - temp1 - temp2
                    node.right.val = res[level] - temp1 - temp2 
                    
                    
                elif node.left and node.right is None:
                    node.left.val = res[level] - node.left.val

                elif node.right and node.left is None:
                    node.right.val = res[level] - node.right.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return root