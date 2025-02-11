"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # Initialize the queue with the root node
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            prev_node = None
            
            # Process all nodes at the current level
            for i in range(level_size):
                node = queue.popleft()
                
                # Connect the previous node's next to the current node
                if prev_node:
                    prev_node.next = node
                prev_node = node
                
                # Enqueue the left and right children of the current node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # The last node's next should be None
            prev_node.next = None

        return root