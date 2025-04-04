# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1

        q = deque([root])
        min_heap = []

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Maintain a min-heap of size k
            heapq.heappush(min_heap, level_sum)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0] if len(min_heap) == k else -1