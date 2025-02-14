# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if root is None:
            return ""
        q = deque()
        q.append(root)
        res = []

        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ",".join(res)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque()
        q.append(root)
        i = 1
        while q:
            cur = q.popleft()
            # Handle left child
            if nodes[i] != "null":
                cur.left = TreeNode(int(nodes[i]))
                q.append(cur.left)
            i += 1
            
            # Handle right child
            if nodes[i] != "null":
                cur.right = TreeNode(int(nodes[i]))
                q.append(cur.right)
            i += 1
        return root

        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans