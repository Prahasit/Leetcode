# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        q = deque()
        q.append((root, 0, 0))
        line_map = defaultdict(lambda: defaultdict(list))

        while q:
            node, x, y = q.popleft()

           
            
            line_map[x][y].append(node.val)

            if node.left:
                q.append((node.left, x - 1, y + 1))
            if node.right:
                q.append((node.right, x + 1, y + 1))

        print(line_map)
        for x in sorted(line_map.keys()):
            col = []
            for  y in sorted(line_map[x].keys()):
                col.extend(sorted(line_map[x][y]))
                print(col)

            ans.append(col)

        return ans

